# SWEA 12712. 파리퇴치3
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXuARWAqDkQDFARa
# 소요시간: 30분 / 시도: 1회

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = []
    plus_mv = [-1, 0, 0, -1, 1, 0, 0, 1]
    mul_mv = [-1, -1, -1, 1, 1, -1, 1, 1]
    result = 0
    
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    for i in range(n):
        for j in range(n):
            
            start = arr[i][j]
            
            for k in range(0, 8, 2):
                for step in range(1, m):
                    if (0 <= i+plus_mv[k]*step < n) and  (0 <= j+plus_mv[k+1]*step < n):
                        start += arr[i+plus_mv[k]*step][j+plus_mv[k+1]*step]
                        
            if result < start:
                result = start
                
            start = arr[i][j]
            
            for k in range(0, 8, 2):
                for step in range(1, m):
                    if (0 <= i+mul_mv[k]*step < n) and  (0 <= j+mul_mv[k+1]*step < n):
                        start += arr[i+mul_mv[k]*step][j+mul_mv[k+1]*step]
                        
            if result < start:
                result = start
                
    print(f"#{test_case} {result}") 