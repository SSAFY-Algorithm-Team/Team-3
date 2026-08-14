# SWEA 2805. 농작물 수확하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB
# 소요시간: 20분 / 시도: 1회

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int,input().strip())) for _ in range(n)]
    mid = n//2
    result = 0
    for i in range(mid):
        result += sum(arr[i][mid-i:mid+i+1])

    result += sum(arr[mid])

    for i in range(mid+1, n):
        result += sum(arr[i][abs(mid-i):mid+n-i])

    print(f'#{test_case} {result}')


# for t in range(1, T + 1):
#     n = int(input())
#     farm = [list(map(int, input().strip())) for _ in range(n)]
# 
#     jump = n // 2
#     answer = 0
# 
#     for row in range(n):
#         for col in range(abs(jump), n - abs(jump)):
#             answer += farm[row][col]
# 
#         jump -= 1  
# 
#     print(f"#{t} {answer}")