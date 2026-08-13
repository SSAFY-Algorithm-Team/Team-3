# SWEA 1289. 원재의 메모리 복구하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN
# 소요시간: 60분 / 시도: 4회

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    memory = list(input())
    n = len(memory)
    init_value = ['0'] * n
    count = 0

    for i in range(n):
        if memory[i] != init_value[i]:
            new_value = memory[i]
            init_value[i:] =  new_value * (n-i)
            count += 1

    print(f'#{test_case} {count}')