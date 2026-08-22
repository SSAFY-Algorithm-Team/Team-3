from typing import List
from collections import deque
import copy

# 테스트 케이스에 대한 초기화 함수
# 길이 유일하므로 road를 뽑아주자(전역변수로 사용)
def init(N : int, mMap : List[List[int]]) -> None:
    global road, field, dr, dc
    global tower_shot_areas
    global tower_reload_times
    global tower_n
    global tower_target
    global tower_attack_ready
    global road_n
    global covering                     # road 칸별로 그 칸을 노리는 타워 목록
    field = copy.deepcopy(mMap)
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    tower_shot_areas = []
    tower_reload_times = []
    tower_n = 0
    # 타워마다 마지막 공격 대상 저장해놓기(-1 : 마지막 공격 대상이 없는 상태)
    tower_target = []                   # [-1]*tower_n 은 tower_n=0 이라 어차피 []
    # 공격 준비 상태 저장해놓기 -> 값은 "다음 공격이 가능해지는 턴"
    tower_attack_ready = []             # 위와 동일

    # start, end 찾기
    start, end = (0, 0), (0, 0)
    for r in range(N):
        for c in range(N):
            if mMap[r][c] == 2:
                start = (r, c)
            if mMap[r][c] == 3:
                end = (r, c)
    road = [start]

    # start에서 시작해서 end까지 길 만들기
    visited = [[False] * N for _ in range(N)]
    tmp = deque()
    tmp.append(start)
    while tmp:
        now = tmp.pop()
        now_r, now_c = now[0], now[1]
        visited[now_r][now_c] = True
        for d in range(4):
            next_r, next_c = now_r + dr[d], now_c + dc[d]
            if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c] and mMap[next_r][next_c] == 3:
                continue
            if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c] and mMap[next_r][next_c] == 1:
                road.append((next_r, next_c))
                tmp.append((next_r, next_c))
    road.append(end)
    road_n = len(road)
    covering = [[] for _ in range(road_n)]   # [수정] 조준 탐색 가속용

# 각 타워들의 사정거리 정보, 쏠 수 있는 영역 저장
def addTower(mRow : int, mCol : int, mInterval : int) -> None:
    global tower_n                      # [수정] tower_n += 1 하려면 필수
    # 타워가 있는 칸은 7로.
    field[mRow][mCol] = 7

    # 타워의 사정거리가 닿는 영역 / 재장전시간을 저장하는 towers
    shot_area = set()                   # [수정] list -> set (in 검사 O(1))
    # 공격거리는 3으로 통일
    N = len(field)
    possible_d = [(0, -3),
                    (-1, -2), (0, -2), (1, -2),
                    (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1),
                    (-3, 0), (-2, 0), (-1, 0), (1, 0), (2, 0), (3, 0),
                    (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1),
                    (-1, 2), (0, 2), (1, 2),
                    (0, 3)]
    for d in possible_d:
        if 0 <= mRow + d[0] < N and 0 <= mCol + d[1] < N:
            shot_area.add((mRow + d[0], mCol + d[1]))

    # [수정] 이 타워가 노릴 수 있는 road 칸을 미리 등록해두면 매턴 전체 스캔을 안 해도 됨
    for r in range(road_n):
        if road[r] in shot_area:
            covering[r].append(tower_n)

    tower_shot_areas.append(shot_area)
    tower_reload_times.append(mInterval)
    tower_target.append(-1)             # [수정] 타워 수만큼 같이 늘려줘야 IndexError 안 남
    tower_attack_ready.append(0)        # [수정] 위와 동일
    tower_n += 1                        # [수정] append 뒤로 옮겨서 인덱스 맞춤

def runSimulation(M : int, mInterval : int, mHP : int, mRetTs : List[int], mRetHP : List[int]) -> None:
    # [수정] runSimulation 은 여러 번 호출되므로 매번 초기화 (게임 시작 시 전 타워 공격 준비 완료)
    for i in range(tower_n):
        tower_target[i] = -1
        tower_attack_ready[i] = 0

    # 도망자info -> [road에서 위치, 남은 체력, 입장순서]
    # [수정] mRetTs/mRetHP 인덱스가 "입장 순서 - 1" 이라 입장순서(pid)를 같이 들고 다녀야 함
    prisoners = []
    by_pid = {}                         # [수정] pid -> 도망자. 타겟을 인덱스로 잡으면 삭제 시 밀림
    generated, t = 0, 0

    # [수정] 모든 도망자가 죽거나 탈출하면 종료
    while generated < M or prisoners:
        t += 1

        # [수정] 사정거리 안에 들어온 도망자만 타워별 후보로 모은다
        # 1. 사정거리 내 대상인지 확인
        # 2. 둘 이상이면, 체력 적은 놈이 타겟
        # 3. 체력도 같으면, 먼저 생성된 놈이 타겟  -> (체력, 입장순서) 튜플 비교로 2,3 동시 처리
        cand = [None] * tower_n
        for p in prisoners:
            for i in covering[p[0]]:
                b = cand[i]
                if b is None or (p[1], p[2]) < (b[1], b[2]):
                    cand[i] = p

        # 타워마다 공격 대상 찾기 -> 우선순위 로직 구현
        for i in range(tower_n):
            # 공격 준비가 안된 타워는 대상을 찾지 않는다 (직전 타겟도 그대로 유지)
            if t < tower_attack_ready[i]:
                continue
            # 직전 공격 대상이 살아있다 + 그 대상이 범위 안에 있으면 유지
            keep = by_pid.get(tower_target[i])
            if keep is not None and road[keep[0]] in tower_shot_areas[i]:
                continue

            # 공격 준비 되었고, 직전 공격 대상이 없다 or 직전 공격대상은 살아있는데 범위 안에 없으면 새로 탐색
            # 못 찾으면 -1 (마지막 공격대상이 없는 상태)
            best = cand[i]
            tower_target[i] = -1 if best is None else best[2]

        # 일괄 공격
        # 준비된 타워는 동시에 타겟을 때린다 (남은 체력보다 많은 공격이 들어갈 수 있음)
        for i in range(tower_n):
            if t < tower_attack_ready[i] or tower_target[i] == -1:
                continue
            by_pid[tower_target[i]][1] -= 1
            # 공격했으면 재장전시간 고려 (재장전 4인 타워가 T=3에 쐈으면 다음은 T=7)
            tower_attack_ready[i] = t + tower_reload_times[i]

        # 만약 hp가 0 이하가 된 도망자가 있다면 삭제 및 턴에 추가
        alive = []                      # [수정] 순회 중 del 하면 인덱스가 밀려서 건너뜀
        for p in prisoners:
            if p[1] <= 0:
                mRetTs[p[2]] = t        # [수정] append 아님. 입장순서 자리에 대입
                mRetHP[p[2]] = 0
                del by_pid[p[2]]
            else:
                alive.append(p)
        prisoners = alive

        # 도망자의 행동주기마다 기존 도망자는 한칸 이동, 새 도망자 생성
        if t % mInterval == 0:          # [수정] t % mInterval 은 "안 나눠떨어질 때" 라 반대였음
            # 도망자 한칸 이동
            for p in prisoners:
                p[0] += 1

            # generated 변수 만들어서 다 생성될때까진 생성도 같이 하기
            # 생성이 덜 됐으면 도망자 생성
            if generated < M:
                p = [0, mHP, generated]
                prisoners.append(p)
                by_pid[generated] = p
                generated += 1          # [수정] 이게 없어서 무한 생성됐음

            # 만약 탈출한 도망자가 있다면 삭제 및 턴에 추가
            # [수정] 이동 직후에 빼야 road[위치] 가 범위를 안 넘음 (원래 IndexError 원인)
            alive = []
            for p in prisoners:
                if p[0] == road_n - 1:
                    mRetTs[p[2]] = t
                    mRetHP[p[2]] = p[1]
                    del by_pid[p[2]]
                else:
                    alive.append(p)
            prisoners = alive