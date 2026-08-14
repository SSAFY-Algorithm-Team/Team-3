# SWEA 11315. 오목 판정
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXaSUPYqPYMDFASQ
# 소요시간: 50분 / 시도: 3회

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())

    possible = False
    
    #나눠서 보기 - 가로
    for i in range(n):
        if 'ooooo' in arr[i] and not possible:
            possible = True
            print(f"#{test_case} YES")
            
	#세로
    if not possible:
        for i in range(n):
            if not possible:
            
                wid_omok = ''
                for j in range(n):
                    wid_omok += arr[j][i]
                
                if 'ooooo' in wid_omok:
                    possible = True
                    print(f"#{test_case} YES")
    
    #대각선
    if not possible:                
        for i in range(n-4):
            for j in range(n-4):
                if arr[i][j] == 'o' and not possible:
                    cross_omok = ''
                    
                    for m in range(5):
                        cross_omok += arr[i+m][j+m]
                        
                    if 'ooooo' in cross_omok and not possible:
                        possible = True
                        print(f"#{test_case} YES")
                        
    if not possible:                
        for i in range(n-4):
            for j in range(4, n):
                if arr[i][j] == 'o' and not possible:
                    cross_omok = ''
                    
                    for m in range(5):  #결국지점마다 5로 생각
                        cross_omok += arr[i+m][j-m]
                        
                    if 'ooooo' in cross_omok and not possible:
                        possible = True
                        print(f"#{test_case} YES")
    
    if not possible:
        print(f"#{test_case} NO")