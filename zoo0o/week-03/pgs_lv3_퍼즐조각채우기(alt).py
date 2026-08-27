# 내 풀이: BFS로 퍼즐을 직사각형 배열로 잘라서 게임보드의 부분 배열과 비교
# 정석 풀이: BFS로 빈칸과 퍼즐의 좌표를 추출하고, 좌표 정규화 + 회전으로 모양 비교

from collections import deque, Counter


def solution(game_board, table):
    n = len(game_board)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 도형을 (0, 0) 기준으로 맞추기
    def normalize(shape):
        min_r = min(r for r, c in shape)
        min_c = min(c for r, c in shape)

        return tuple(sorted((r - min_r, c - min_c) for r, c in shape))

    # 연결된 도형 찾기
    def find_shapes(board, target):
        visited = [[0] * n for _ in range(n)]
        shapes = []

        for start_r in range(n):
            for start_c in range(n):
                if board[start_r][start_c] != target:
                    continue
                if visited[start_r][start_c]:
                    continue

                queue = deque([(start_r, start_c)])
                visited[start_r][start_c] = 1
                shape = []

                while queue:
                    r, c = queue.popleft()
                    shape.append((r, c))

                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]

                        if 0 <= nr < n and 0 <= nc < n:
                            if board[nr][nc] == target and not visited[nr][nc]:
                                visited[nr][nc] = 1
                                queue.append((nr, nc))

                shapes.append(normalize(shape))

        return shapes

    # 90도 회전
    def rotate(shape):
        rotated = [(c, -r) for r, c in shape]
        return normalize(rotated)

    # 4번 회전 중 대표 모양 선택
    def get_shape_key(shape):
        rotations = []
        current = shape

        for _ in range(4):
            rotations.append(current)
            current = rotate(current)

        return min(rotations)

    # 게임보드의 0 = 빈 공간
    holes = find_shapes(game_board, 0)

    # 테이블의 1 = 퍼즐
    puzzles = find_shapes(table, 1)

    puzzle_count = Counter()

    for puzzle in puzzles:
        puzzle_count[get_shape_key(puzzle)] += 1

    answer = 0

    # 같은 모양의 퍼즐이 있으면 채우기
    for hole in holes:
        key = get_shape_key(hole)

        if puzzle_count[key] > 0:
            answer += len(hole)
            puzzle_count[key] -= 1

    return answer
