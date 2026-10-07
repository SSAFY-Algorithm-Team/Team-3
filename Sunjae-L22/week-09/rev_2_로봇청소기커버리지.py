# 로봇청소기커버리지
# 소요시간 : 45분 + 30분

# BFS
from collections import deque


def solution(n, robots, walls):
    # 벽 -> walls 좌표 사용해서 두 쪽 가는거 막힘
    blocked = set()
    for r1, c1, r2, c2 in walls:
        blocked.add((r1, c1, r2, c2))
        blocked.add((r2, c2, r1, c1))

    dist = [[-1] * (n + 1) for _ in range(n + 1)]
    queue = deque()

    # 로봇이 있는 좌표 -> 거리 0 넣어주기
    for r, c in robots:
        if dist[r][c] == -1:
            dist[r][c] = 0
            queue.append((r, c))

    # 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = 0

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # 범위 확인
            if not (1 <= nr <= n and 1 <= nc <= n):
                continue

            # 이미 로봇청소기가 지나간 지점이라면 지나가기
            if dist[nr][nc] != -1:
                continue

            # 지나갈 수 없는 경로면 
            if (r, c, nr, nc) in blocked:
                continue

            dist[nr][nc] = dist[r][c] + 1
            answer = max(answer, dist[nr][nc])
            queue.append((nr, nc))

    return answer


# 코테 때 내가 했던 풀이
def solution(n, robots, walls):
    blocked = set()
    for r1, c1, r2, c2 in walls:
        blocked.add((r1, c1, r2, c2))
        blocked.add((r2, c2, r1, c1))

    # 로봇 청소기가 지나간 지점을 cleaned로 두기
    cleaned = set(map(tuple, robots))
    time = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 사무실의 모든 칸이 청소될때까지!!
    while len(cleaned) < n * n:
        # 이번 시간이 시작될 때 청소되어 있던 칸들
        current = list(cleaned)

        for r, c in current:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (1 <= nr <= n and 1 <= nc <= n):
                    continue

                if (r, c, nr, nc) in blocked:
                    continue

                cleaned.add((nr, nc))

        time += 1

    return time