# SWEA 11315. 오목 판정
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXaSUPYqPYMDFASQ
# 소요시간: 20분 / 시도: 1회

def bfs(n, x, y, count, dir_vec):
    global isValid

    if count >= 5:
        isValid = True
        return

    if x < 0 or y < 0 or x > n - 1 or y > n - 1:
        return

    if field[x][y] != 'o':
        return
    else:
        count += 1

    bfs(n, x + dir_vec[0], y + dir_vec[1], count, dir_vec)


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    field = [list(map(str, input())) for _ in range(n)]
    dir_arr = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    isValid = False

    for i in range(n):
        for j in range(n):
            for dir_vec in dir_arr:
                count = 0
                bfs(n, i, j, count, dir_vec)

    if isValid:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")
