from collections import deque

def solution(n, robots, walls):

    # 상하좌우 이동
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 칸 사이에 벽을 표현하기 위해 맵을 2배로 확장
    size = 2 * n - 1
    maps = [[0] * size for _ in range(size)]

    robots2 = []

    # 로봇 좌표를 0-index 기준으로 바꾸고 2배 확장
    for r, c in robots:
        r = (r - 1) * 2
        c = (c - 1) * 2

        maps[r][c] = 2
        robots2.append((r, c))

    # 벽은 연결된 두 칸의 중간 좌표에 표시
    for r1, c1, r2, c2 in walls:
        r1 = (r1 - 1) * 2
        c1 = (c1 - 1) * 2
        r2 = (r2 - 1) * 2
        c2 = (c2 - 1) * 2

        r = (r1 + r2) // 2
        c = (c1 + c2) // 2

        maps[r][c] = 1

    queue = deque()

    # 각 위치까지 가장 가까운 로봇의 거리를 저장
    visited = [[-1] * size for _ in range(size)]

    # 모든 로봇을 동시에 BFS 시작점으로 넣음
    for r, c in robots2:
        queue.append((r, c))
        visited[r][c] = 0

    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 맵 범위를 벗어나면 이동 불가
            if nr < 0 or nr >= size or nc < 0 or nc >= size:
                continue

            # 이미 방문한 위치는 다시 확인하지 않음
            if visited[nr][nc] != -1:
                continue

            # 벽이 있는 위치는 지나갈 수 없음
            if maps[nr][nc] == 1:
                continue

            # 홀수, 홀수 위치는 실제 칸이나 통로가 아니므로 이동 불가
            if nr % 2 == 1 and nc % 2 == 1:
                continue

            visited[nr][nc] = visited[r][c] + 1
            queue.append((nr, nc))

    result = 0

    # 실제 사무실 칸인 짝수, 짝수 좌표만 확인
    for r in range(0, size, 2):
        for c in range(0, size, 2):

            # 확장 맵에서는 실제 한 칸 이동이 거리 2이므로 2로 나눔
            result = max(result, visited[r][c] // 2)

    return result