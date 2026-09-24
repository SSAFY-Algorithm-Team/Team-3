# SWEA 4828. [S/W 문제해결 기본] 1일차 - min max
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZ9kDS86wCTHBITH&contestProbId=AWTLQZwKon4DFAVT&probBoxId=AZ9kDS86wCXHBITH&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+%EA%B8%B0%EB%B3%B8&problemBoxCnt=6

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))

    answer = max(a) - min(a)
    print(f'#{tc} {answer}')