# SWEA 25052. 등산로
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZiyl6OKpUjHBIP9
# 소요시간: 45분 / 시도: 3회

t = int(input())

def get_length(start_row, start_col):
    row = start_row
    col = start_col

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1] 
    length = 1
    while True:
        next_row = row
        next_col = col
        lowest = matrix[row][col]

        for d in range(4): 
            nr = row + dr[d]
            nc = col + dc[d]

            if 0 <= nr < n and 0 <= nc < n:
                if matrix[nr][nc] < lowest: 
                    lowest = matrix[nr][nc] 
                    next_row = nr
                    next_col = nc

        if next_row == row and next_col == col:
            break

        row = next_row
        col = next_col
        length += 1

    return length

for test_case in range(1,t+1):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    max_length = 0
    for row in range(n):
        for col in range(n):
            max_length = max(max_length, get_length(row,col))

    print(f'#{test_case} {max_length}')

