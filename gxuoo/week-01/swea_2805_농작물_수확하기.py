# SWEA 2805. 농작물 수확하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB
# 소요시간: 30분 / 시도: 4회

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    field = [list(map(int, input())) for _ in range(n)]
    total = 0

    for i in range(n // 2):
        for j in range(n // 2 - i, n // 2 + i + 1):
            total += field[i][j]

    for i in range(n // 2, n):
        for j in range(i - n // 2, n - (i - n // 2)):
            total += field[i][j]

    print(f"#{test_case} {total}")
