# SWEA 26045. 부분 수열 판별
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZwe0FZaG1bHBIPa
# 소요시간: 10분 / 시도: 1회

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    
    for b in B:
        for a in range(len(A)):
            if b == A[a]:
                count += 1
                break
                
        A = A[a+1:]
    
    if count == m:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")
