# SWEA 1959. 두개의 숫자열
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq
# 소요시간: 10분 / 시도: 1회

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    if n>= m:
        long, small = arr1, arr2
    else:
        long, small = arr2, arr1
    
    l, s = len(long), len(small)
    sum = -9999999999
	
    for i in range(l-s+1):
        semi_sum = 0
        
        for j in range(s):
            semi_sum += long[i+j] * small[j]
        if sum < semi_sum:
            sum = semi_sum
            
    print(f"#{test_case} {sum}")