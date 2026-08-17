from collections import deque

T = int(input())


# 현재 벽돌 상태와 구슬을 떨구는 위치가 주어지면, 이후 벽돌 상태를 반환하는 함수
# bricks : W * H 
# bead_loc : 0 ~ W-1 범위에 떨어질 수 있음
def drop(bricks, W, H, bead_loc):
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 구슬이 처음 떨어지는 위치 찾아서 터지는 벽돌 큐에 넣기
    broken_bricks = deque()
    for i in range(H-1, -1, -1):
        # 0이 아닐 때
        if bricks[bead_loc][i] != 0:
            broken_bricks.append((bead_loc, i))
            break

    # 더이상 깨질 게 없을 때까지 반복
    while broken_bricks:
        now_row, now_col = broken_bricks.popleft()

        # 만약 벽돌의 숫자가 1이면 혼자 깨지고, 깨진 곳 0으로 변경
        if bricks[now_row][now_col] == 1:
            bricks[now_row][now_col] = 0
            continue

        # 벽돌의 숫자가 2 이상이면 폭발 범위의 벽돌을 broken_bricks에 추가, 깨진 곳은 0으로 변경
        else:
            for scope in range(1, bricks[now_row][now_col]):
                bricks[now_row][now_col] = 0
                for dir in range(4):
                    next_row = now_row + scope * dr[dir]
                    next_col = now_col + scope * dc[dir]
                    # 만약 bricks 인덱스 내에 있고 벽돌 숫자가 1 이상이면 추가
                    if 0 <= next_row < W and 0 <= next_col < H and bricks[next_row][next_col] >= 1:
                        broken_bricks.append((next_row, next_col))

    # 깨질만큼 다 깨졌으면 중력에 의해 빈 공간을 채우는 로직
    returning_bricks = [[0] * H for _ in range(W)]
    for row in range(W):
        count = 0
        for col in range(H):
            if bricks[row][col] > 0:
                returning_bricks[row][count] = bricks[row][col]
                count += 1

    return returning_bricks
    

# 벽돌 상태가 주어지면 남은 벽돌의 개수 반환하는 함수
def remain(bricks):
    W = len(bricks)
    H = len(bricks[0])
    brick_n = 0

    for row in range(W):
        for col in range(H):
            # 만약 벽돌이 있으면 brick_n += 1
            if bricks[row][col]:
                brick_n += 1

    return brick_n


# 구슬 N개를 떨어뜨리는 순서(중복순열)를 반환하는 함수
def drop_sequence(N, W):
    result, path = [], []

    def dfs(depth):
        if depth == N:
            result.append(path[:])
            return
        for i in range(W):
            path.append(i)
            dfs(depth+1)
            path.pop()

    dfs(0)
    return result


for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks_origin = [list(map(int, input().split())) for _ in range(H)]
    bricks = [[0] * H for _ in range(W)]

    # row 단위로 생각하는게 편해서 벽돌 행렬 시계방향 90도 돌리기
    # 이러면 이후부터 W가 row 개수, H가 col 개수라고 생각하면 됨 
    for row in range(W):
        for col in range(H):
            bricks[row][col] = bricks_origin[H - 1 - col][row]

    # drop_sequence를 돌며 남은 벽돌 최소값 찾기
    answer = W * H
    # N = 3일 때 drop_sequence ex) [[0, 0, 0], [0, 0, 1], [0, 0, 2], ...]
    for sequence in drop_sequence(N, W):
        # 순서 시작할때마다 실험용 bricks_ex에 원본 bricks를 복사 -> 깊은 복사
        bricks_ex = [row[:] for row in bricks]
        # sequence는 [0, 1, 2] 형태
        for bead_loc in sequence:
            bricks_ex = drop(bricks_ex, W, H, bead_loc)
        # 남은 벽돌 개수 세고, 기존 answer과 비교 후 작은 걸 answer에 저장
        answer = min(answer, remain(bricks_ex))
        # 다 깨졌으면 무조건 0이니까 시간 절약 가능
        if answer == 0:
            break

    print(f"#{tc} {answer}")