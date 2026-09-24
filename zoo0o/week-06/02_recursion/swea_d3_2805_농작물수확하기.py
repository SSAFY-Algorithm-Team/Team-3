# SWEA 2805. 농작물 수확하기
# https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawC3HBITH

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]

    center = N // 2
    answer = 0

    for r in range(N):
        gap = abs(center - r)

        for c in range(gap, N - gap):
            answer += maps[r][c]

    print(f'#{tc} {answer}')