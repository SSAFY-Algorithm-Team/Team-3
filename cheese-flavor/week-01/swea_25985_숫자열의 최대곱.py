# SWEA 25985. 숫자열의 최대곱
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZvmEUAqG6LHBIQE
# 소요시간: 50분 / 시도: 1회

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    max_sum = -99999999999
    
    if len(arr1) <= len(arr2):   # m = len(long)
        long, short = arr2, arr1
    else:
        long, short, m, n = arr1, arr2, n, m 
        
    short_index = []
    for i in range(1, n+1):
        short_index.append(i - n)
    
    for _ in range(n+m-1):
        semi_sum = 0
        
        for s in range(n):
            for l in range(m):
                if short_index[s] == l:
                    semi_sum += (short[s] * long[l])
            
            short_index[s] += 1
            
        max_sum = max(max_sum, semi_sum)
    
    print(f"#{test_case} {max_sum}")
