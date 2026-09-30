# ==============================================
# 코드 제출시 아래 2줄은 반드시 주석처리 하여 제출
# import sys
# sys.stdin = open('algo1_sample_in.txt')
# ==============================================

# 아래에 코드를 작성하세요.

from collections import deque
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
T = int(input())

for tc in range(1, T+1):
    # 건물 정보 입력받기
    N, M = map(int, input().split())
    floor = []
    for i in range(N):
        floor.append(list(map(int, input().split())))

    # 출발 위치 찾기
    start_r, start_c = 0, 0
    for r in range(N):
        for c in range(M):
            if floor[r][c] == 3:
                start_r, start_c = r, c

    # 최단거리니까 BFS로 풀어봅시다
    # used : 도끼 사용여부
    q = deque([(start_r, start_c, False)])
    distance = [[0] * M for _ in range(N)]

    while q:
        r, c, used = q.popleft()
        for d in range(4):
            # 도끼를 사용했다면 벽(1)있는곳 못감
            if used:
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < M and floor[nr][nc] in (0, 2) and distance[nr][nc] == 0:
                    q.append((nr, nc, True))
                    distance[nr][nc] = distance[r][c] + 1
            # 도끼를 사용하지 않았다면 1인 곳도 갈수있음
            else:
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < M and floor[nr][nc] in (0, 1, 2) and distance[nr][nc] == 0:
                    # floor[nr][nc]가 1이면 벽을 뚫은거니까 도끼 사용으로 append
                    if floor[nr][nc] == 1:
                        q.append((nr, nc, True))
                    else:
                        q.append((nr, nc, False))
                    distance[nr][nc] = distance[r][c] + 1

    # 가장 가까운 출구 찾기
    answer = 10001
    for r in range(N):
        for c in range(M):
            if floor[r][c] == 2 and distance[r][c] > 0:
                answer = min(answer, distance[r][c])
    if answer == 10001:
        answer = -1
    print(f"#{tc} {answer}")