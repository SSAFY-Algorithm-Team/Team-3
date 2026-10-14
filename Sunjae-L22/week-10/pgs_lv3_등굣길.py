# 프로그래머스 Lv3. 등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 소요시간: 30분 / 시도: 7

def solution(m, n, puddles):
    MOD = 1_000_000_007
    # m = 가로(열), n = 세로(행)
    area = [[0] * (m + 1) for _ in range(n + 1)]
    water = {(x, y) for x, y in puddles}   # [x, y] = [열, 행]

    area[1][1] = 1
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if (x, y) == (1, 1):
                continue
            if (x, y) in water:
                area[y][x] = 0
                continue
            area[y][x] = (area[y-1][x] + area[y][x-1]) % MOD
    return area[n][m]


print(4, 3, [[2, 2]])