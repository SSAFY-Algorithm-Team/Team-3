# 프로그래머스 Lv3. 등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 소요시간: 60분 / 시도: 10회?

def solution(m, n, puddles):
    board = [[1]*m for _ in range(n)]

    for pc, pr in puddles:
        board[pr-1][pc-1] = 0
        if pc == 1:
            for i in range(pr-1,n):
                board[i][0] = 0
        elif pr == 1: 
            for i in range(pc-1,m):
                board[0][i] = 0
    for row in range(n):
        for col in range(m):
            if 0 <= row < n and 0 <= col < m and board[row][col] != 0:
                if row != 0 and col != 0:
                    board[row][col] = board[row-1][col] + board[row][col-1]

    result = board[n-1][m-1] % 1000000007
    print(result)
    return result



solution(4, 3, [[2, 2]])