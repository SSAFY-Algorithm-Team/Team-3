# 프로그래머스 Lv3. 퍼즐 조각 채우기
# https://school.programmers.co.kr/learn/courses/30/lessons/84021
# 구현 > AI

from collections import deque


def solution(game_board, table):
    n = len(game_board)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 1. table에서 연결된 퍼즐 하나를 BFS로 찾고
    #    퍼즐이 들어가는 최소 직사각형 배열로 만든다.
    def make_puzzle(start_r, start_c, visited):
        queue = deque()
        queue.append((start_r, start_c))
        visited[start_r][start_c] = 1

        cells = []

        while queue:
            r, c = queue.popleft()
            cells.append((r, c))

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < n and 0 <= nc < n:
                    if table[nr][nc] == 1 and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))

        # 퍼즐이 존재하는 범위 찾기
        min_r = min(r for r, c in cells)
        max_r = max(r for r, c in cells)
        min_c = min(c for r, c in cells)
        max_c = max(c for r, c in cells)

        height = max_r - min_r + 1
        width = max_c - min_c + 1

        puzzle = [[0] * width for _ in range(height)]

        for r, c in cells:
            puzzle[r - min_r][c - min_c] = 1

        return puzzle

    visited_table = [[0] * n for _ in range(n)]
    puzzles = []

    # table 전체를 돌면서 퍼즐 하나씩 추출
    for r in range(n):
        for c in range(n):
            if table[r][c] == 1 and visited_table[r][c] == 0:
                puzzle = make_puzzle(r, c, visited_table)
                puzzles.append(puzzle)

    # 2. 퍼즐을 시계 방향으로 90도 회전
    def rotate(puzzle):
        row_size = len(puzzle)
        col_size = len(puzzle[0])

        rotated = [[0] * row_size for _ in range(col_size)]

        for r in range(row_size):
            for c in range(col_size):
                rotated[c][row_size - 1 - r] = puzzle[r][c]

        return rotated

    # game_board에서 이미 퍼즐을 채운 칸
    filled = [[0] * n for _ in range(n)]

    def get_board_value(r, c):
        # 원래 1이거나 이미 퍼즐을 넣은 칸이면
        # 채워진 칸 1로 취급
        if game_board[r][c] == 1 or filled[r][c] == 1:
            return 1

        return 0

    # 3. 퍼즐과 game_board의 직사각형 영역 비교
    def can_place(puzzle, start_r, start_c):
        height = len(puzzle)
        width = len(puzzle[0])

        puzzle_cells = set()

        for pr in range(height):
            for pc in range(width):
                br = start_r + pr
                bc = start_c + pc

                board = get_board_value(br, bc)

                # puzzle과 game_board가 서로 반대여야 함
                #
                # puzzle 1 + board 0 -> XOR 1
                # puzzle 0 + board 1 -> XOR 1
                #
                # 전부 XOR 결과가 1이어야 딱 맞음
                if (puzzle[pr][pc] ^ board) != 1:
                    return False

                if puzzle[pr][pc] == 1:
                    puzzle_cells.add((br, bc))

        # 퍼즐을 놓은 뒤 상하좌우에 빈칸이 남으면 안 됨
        for r, c in puzzle_cells:
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) not in puzzle_cells:
                        if get_board_value(nr, nc) == 0:
                            return False

        return True

    answer = 0

    # 4. puzzles에서 하나씩 꺼내서 게임보드와 비교
    for puzzle in puzzles:
        current = puzzle
        placed = False

        # 0도 / 90도 / 180도 / 270도
        for _ in range(4):
            height = len(current)
            width = len(current[0])

            # 퍼즐 크기만큼 game_board를 잘라서 비교
            for r in range(n - height + 1):
                if placed:
                    break

                for c in range(n - width + 1):
                    if can_place(current, r, c):

                        # 퍼즐이 들어간 칸 사용 처리
                        for pr in range(height):
                            for pc in range(width):
                                if current[pr][pc] == 1:
                                    filled[r + pr][c + pc] = 1

                        # puzzle에서 1의 개수 = 채운 칸 수
                        answer += sum(sum(row) for row in current)

                        placed = True
                        break

            if placed:
                break

            current = rotate(current)

    return answer
