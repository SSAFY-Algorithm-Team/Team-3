# SWEA 1289. 원재의 메모리 복구하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN
# 소요시간: 60분 / 시도: 4회

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    memory = input().strip()
    current = '0'
    count = 0

    for bit in memory:
        if bit != current:
            count += 1
            current = bit

    print(f'#{test_case} {count}')