# SWEA 2805. 농작물 수확하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB
# 소요시간: 30분 / 시도: 1회

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())
    
    sector = n//2 #구조를 분리할 값
    
    middle, up, down = 0, 0, 0    #중
    for i in range(n):
        middle += int(arr[sector][i])    
        
    if n != 1:
        up = int(arr[0][sector])   #상
        for i in range(1, sector):
            up += int(arr[i][sector])

            for j in range(1, i+1):
                up += int(arr[i][sector-j]) + int(arr[i][sector+j])

        down = int(arr[n-1][sector])  #하
        for i in range(n-2, sector, -1):
            down += int(arr[i][sector])
            
            for j in range(1, n-i):
                down += int(arr[i][sector-j]) + int(arr[i][sector+j])
        
    print(f"#{test_case} {up+down+middle}")