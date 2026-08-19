# SWEA 5656. 벽돌 깨기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo
# 소요시간: 4시간 / 시도: 2회


from collections import deque

# 상하좌우 4방향 이동량
DELTA_ROW = [-1, 1, 0, 0]
DELTA_COL = [0, 0, -1, 1]


def explode(board, height, width, target_col):
    """target_col에 구슬을 떨어뜨려 연쇄 폭발을 처리한다 (board를 직접 수정)."""
    # 해당 열에서 위에서부터 처음 만나는 벽돌의 행 = 구슬이 맞히는 지점
    hit_row = -1
    for row in range(height):
        if board[row][target_col]:
            hit_row = row
            break
    if hit_row == -1:
        return  # 빈 열이라 아무 일도 일어나지 않음

    blast_queue = deque([(hit_row, target_col)])
    is_queued = [[False] * width for _ in range(height)]
    is_queued[hit_row][target_col] = True

    while blast_queue:
        row, col = blast_queue.popleft()
        blast_range = board[row][col]   # 벽돌 숫자 = 폭발 범위
        board[row][col] = 0             # 이 벽돌은 깨짐

        for direction in range(4):
            for distance in range(1, blast_range):
                next_row = row + DELTA_ROW[direction] * distance
                next_col = col + DELTA_COL[direction] * distance

                # 격자 밖 → 이 방향은 더 볼 필요 없음
                if not (0 <= next_row < height and 0 <= next_col < width):
                    break

                # 빈칸은 통과해서 계속 뻗어나감
                if is_queued[next_row][next_col] or board[next_row][next_col] == 0:
                    continue

                is_queued[next_row][next_col] = True
                blast_queue.append((next_row, next_col))


def apply_gravity(board, height, width):
    """폭발 후 공중에 뜬 벽돌을 아래로 내린다 (board를 직접 수정)."""
    for col in range(width):
        # 이 열에 남아 있는 벽돌만 위에서 아래 순서로 모은다
        remaining_bricks = []
        for row in range(height):
            if board[row][col]:
                remaining_bricks.append(board[row][col])

        empty_count = height - len(remaining_bricks)

        # 위쪽은 빈칸으로
        for row in range(empty_count):
            board[row][col] = 0

        # 아래쪽에 순서대로 채움
        for offset, brick in enumerate(remaining_bricks):
            board[empty_count + offset][col] = brick


def count_bricks(board):
    """격자에 남아 있는 벽돌 개수."""
    total = 0
    for row in range(height):
        for col in range(width):
            if board[row][col]:
                total += 1
    return total


def search(board, shots_used):
    """구슬을 남김없이 쏘는 모든 경우를 탐색해 최소 잔여 벽돌 수를 갱신한다."""
    global answer

    if shots_used == total_shots:
        answer = min(answer, count_bricks(board))
        return

    for col in range(width):
        next_board = [row[:] for row in board]   # 분기마다 독립된 사본 사용
        explode(next_board, height, width, col)
        apply_gravity(next_board, height, width)
        search(next_board, shots_used + 1)


test_count = int(input())

for test_case in range(1, test_count + 1):
    total_shots, width, height = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(height)]

    answer = height * width
    search(board, 0)

    print(f"#{test_case} {answer}")
