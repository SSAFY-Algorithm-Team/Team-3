# SWEA 3499. 퍼펙트 셔플
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW
# 소요시간: 15분 / 시도: 1회

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(input().split())
    arr_n = 0
    
    if n % 2 == 0:
        arr_n = n//2
    else:
        arr_n = n//2 + 1
    
    arr1 = arr[:arr_n]
    arr2 = arr[arr_n:]
    new_arr = ''
    
    for i in range(arr_n):
        new_arr += (arr1[i])
        if n % 2 == 0 or i != arr_n-1:
            new_arr += ' '
        
        if i < len(arr2):
            new_arr += (arr2[i]) + ' '
            
    print(f"#{test_case} {new_arr}")
        
