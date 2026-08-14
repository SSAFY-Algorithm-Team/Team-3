# SWEA 1979. 어디에 단어가 들어갈 수 있을까
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq
# 소요시간: 40분 / 시도: 1회

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = []
    route = 0
    
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    for i in range(n):
        for j in range(n):
            
            # 가로로 시작
            if arr[i][j] == 1 and j+k <= n:
                if j == 0 or arr[i][j-1] == 0:          # 이전도 0인지
                    count = 1
                    
                    for m in range(1, k):
                        if arr[i][j+m] == 0:
                            break
                        count += 1
                    
                    if count == k:
                        if j+k == n or arr[i][j+k] == 0:  # 이후가 0인지
                            route += 1
                    
            # 세로 시작
            if arr[i][j] == 1 and i+k <= n:
                if i == 0 or arr[i-1][j] == 0:          
                    count = 1
                    
                    for m in range(1, k):
                        if arr[i+m][j] == 0:
                            break
                        count += 1
                    
                    if count == k:
                        if i+k == n or arr[i+k][j] == 0: 
                            route += 1
                    
    print(f"#{test_case} {route}")