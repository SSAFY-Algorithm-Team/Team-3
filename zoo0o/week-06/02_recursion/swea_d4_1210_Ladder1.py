# SWEA 1210. Ladder1
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZ9kDS86wCTHBITH&contestProbId=AV14ABYKADACFAYh&probBoxId=AZ9kECgawC3HBITH&type=PROBLEM&problemBoxTitle=%EC%9E%AC%EA%B7%80&problemBoxCnt=4

import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    tc = int(input())
    maps = [list(map(int, input().split())) for _ in range(100)]

    visited = [[False] * 100 for _ in range(100)]

    row = 99
    col = 0

    # 1. 도착점 2 찾기
    for i in range(100):
        if maps[99][i] == 2:
            col = i
            break

    visited[row][col] = True

    # 2. 도착점에서 위로 이동
    while row:

        # 왼쪽으로 이동
        if col > 0 and maps[row][col - 1] == 1 and not visited[row][col - 1]:
            col -= 1

        # 오른쪽으로 이동
        elif col < 99 and maps[row][col + 1] == 1 and not visited[row][col + 1]:
            col += 1

        # 좌우 길이 없으면 위로 이동
        else:
            row -= 1

        visited[row][col] = True

    print(f'#{tc} {col}')