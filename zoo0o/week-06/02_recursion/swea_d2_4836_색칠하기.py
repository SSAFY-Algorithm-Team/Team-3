# SWEA 4836. [S/W 문제해결 기본] 2일차 - 색칠하기
# https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZ9kDS86wCTHBITH&probBoxId=AZ9kECgawC3HBITH

import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maps = [[0] * 10 for _ in range(10)]

    for i in range(N):
        for r in range(arr[i][0], arr[i][2]+1):
            for c in range(arr[i][1], arr[i][3]+1):
                # 비트 or 연산
                maps[r][c] |= arr[i][4]

    # 비트가 11인 개수 세기
    answer = 0

    for r in range(10):
        for c in range(10):
            if maps[r][c] == 3:
                answer += 1

    print(f'#{tc} {answer}')