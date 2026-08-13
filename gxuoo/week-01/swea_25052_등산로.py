# SWEA 25052. 등산로
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZiyl6OKpUjHBIP9
# 소요시간: 1시간 / 시도: 3회

dir_row = (-1, 1, 0, 0)
dir_col = (0, 0, -1, 1)

def find_next(row, col):
    lowest = h_field[row][col]
    next_row, next_col = -1, -1

    for dir_idx in range(4):
        calc_row = row + dir_row[dir_idx]
        calc_col = col + dir_col[dir_idx]
        if 0 <= calc_row < n and 0 <= calc_col < n and h_field[calc_row][calc_col] < lowest:
            lowest = h_field[calc_row][calc_col]
            next_row, next_col = calc_row, calc_col

    return next_row, next_col

def check(row, col, length):
    global max_len
    if length > max_len:
        max_len = length

    next_row, next_col = find_next(row, col)
    if next_row == -1:
        return
    check(next_row, next_col, length + 1)

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    h_field = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for row in range(n):
        for col in range(n):
            max_len = 0
            check(row, col, 1)

            if max_len > result:
                result = max_len

    print(f'#{test_case} {result}')
