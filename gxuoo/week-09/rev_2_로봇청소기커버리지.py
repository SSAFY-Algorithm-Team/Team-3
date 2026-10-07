# 복기 2. 로봇청소기 커버리지
# 소요시간: 80분 / 시도: 5회

from collections import deque

drs = [0, 0, 1, -1]
dcs = [1, -1, 0, 0]

def solution(n, robots, walls):
    # BFS를 사용하되, 벽에 대한 처리를 리스트로 하면 시간초과가 날 것 같음
    # set을 쓰면 조금 나아질까..?

    answer = 0
    field = [[-1] * (n + 1) for _ in range(n + 1)]
    blocked = set()
    
    for r1, c1, r2, c2 in walls:
        blocked.add((r1, c1, r2, c2))
        blocked.add((r2, c2, r1, c1))

    def BFS(robots):
        queue = deque()

        for row, col in robots:
            field[row][col] = 0
            queue.append((row, col))

        while queue:
            r, c = queue.popleft()

            for dr, dc in zip(drs, dcs):
                nr = r + dr
                nc = c + dc

                # 범위 안에 있는지
                if 1 <= nr <= n and 1 <= nc <= n:
                    # 다음에 이동할 곳에 벽이 없는지
                    if (r, c, nr, nc) in blocked:
                        continue
                    # 방문한 적이 없는지
                    elif field[nr][nc] != -1:
                        continue
                    else:
                        field[nr][nc] = field[r][c] + 1
                        queue.append((nr, nc))


    BFS(robots)

    # 모든 칸을 돌면서 가장 먼 거리를 찾음
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if field[r][c] > answer:
                answer = field[r][c]

    return answer


if __name__ == "__main__":
    print(solution(3, [[1, 1]], []))  # 4
    print(solution(5, [[1, 1], [5, 5]], []))  # 4
    walls = [[3, 4, 4, 4], [3, 5, 4, 5], [5, 4, 6, 4], [5, 5, 6, 5],
             [4, 3, 4, 4], [5, 3, 5, 4], [4, 5, 4, 6],
             [2, 2, 2, 3], [2, 6, 2, 7], [7, 2, 7, 3], [7, 6, 7, 7],
             [1, 4, 1, 5], [8, 4, 8, 5]]
    print(solution(8, [[1, 1], [1, 8], [8, 1], [8, 8]], walls))  # 8
