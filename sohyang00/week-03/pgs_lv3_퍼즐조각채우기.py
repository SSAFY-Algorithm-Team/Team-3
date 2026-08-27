# 프로그래머스 Lv3. 퍼즐 조각 채우기
# https://school.programmers.co.kr/learn/courses/30/lessons/84021
directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

def solution(game_board, table):
    n = len(game_board)

    def extract_shapes(grid, target):
        visited = [[False] * n for _ in range(n)]
        shapes = []

        def dfs(row, col, shape):
            visited[row][col] = True
            shape.append((row, col))

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and not visited[nr][nc]
                    and grid[nr][nc] == target
                ):
                    dfs(nr, nc, shape)

        for row in range(n):
            for col in range(n):
                if grid[row][col] == target and not visited[row][col]:
                    shape = []
                    dfs(row, col, shape)
                    shapes.append(normalize(shape))

        return shapes

    def normalize(shape):
        min_row = min(row for row, col in shape)
        min_col = min(col for row, col in shape)

        normalized = []

        for row, col in shape:
            normalized.append(
                (row - min_row, col - min_col)
            )

        return sorted(normalized)

    def rotate(shape):
        rotated = []

        for row, col in shape:
            rotated.append((col, -row))

        return normalize(rotated)

    # 보드 0 빈 공간
    blanks = extract_shapes(game_board, 0)

    # 테이블 1 퍼즐
    puzzles = extract_shapes(table, 1)

    used = [False] * len(puzzles)
    answer = 0

    for blank in blanks:
        for i in range(len(puzzles)):
            if used[i]:
                continue

            if len(blank) != len(puzzles[i]):
                continue

            puzzle = puzzles[i]

            # 0도, 90도, 180도, 270도 확인
            for _ in range(4):
                if blank == puzzle:
                    used[i] = True
                    answer += len(blank)
                    break

                puzzle = rotate(puzzle)

            # 현재 빈 공간에 퍼즐을 넣었다면
            # 다른 퍼즐은 확인하지 않음
            if used[i]:
                break

    return answer
