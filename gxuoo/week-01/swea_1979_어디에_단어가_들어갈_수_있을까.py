# SWEA 1979. 어디에 단어가 들어갈 수 있을까
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq
# 소요시간: 25분 / 시도: 2회

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for i in range(n):
        row_count = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                row_count += 1
            else:
                if row_count == k:
                    count += 1
                row_count = 0
        if row_count == k:
            count += 1
    for j in range(n):
        col_count = 0
        for i in range(n):
            if puzzle[i][j] == 1:
                col_count += 1
            else:
                if col_count == k:
                    count += 1
                col_count = 0
        if col_count == k:
            count += 1

    print(f"#{test_case} {count}")
