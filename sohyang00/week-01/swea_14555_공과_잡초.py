# SWEA 14555. 공과 잡초
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYGtoa3qARcDFARC
# 소요시간: 20분 / 시도: 1회

import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = input().strip()
    stack = []
    count = 0

    for i in arr:
        if i == '(': # 굳이... 처리를 해야할까? 걍 다 넣자
            stack.append('(')
        elif i == ')':
            if not stack: 
                continue
            else: 
                tmp = stack.pop()
                if tmp == '(':
                    count += 1
                elif tmp == '|':
                    count += 1
        elif i == '|':
            if not stack: 
                stack.append('|')
            else: 
                tmp = stack.pop()
                if tmp == '(':
                    count += 1
                elif tmp == '|':
                    stack.append('|')
        else: # . 일때 ... 
            continue
    print(f'#{test_case} {count}')

