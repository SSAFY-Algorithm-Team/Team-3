# SWEA 14555. 공과 잡초
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYGtoa3qARcDFARC
# 소요시간: 20분 / 시도: 1회

import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = input().strip()
    count = 0

    for i in range(len(arr) - 1):
        if arr[i:i+2] in ('()', '(|', '|)'):
            count += 1

    print(f'#{test_case} {count}')

