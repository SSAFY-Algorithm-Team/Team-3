# SWEA 25052. 등산로
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZiyl6OKpUjHBIP9
# 소요시간: 50분 / 시도: 1회

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    def road(i, j):
        mv = [-1, 0 ,1, 0, 0, -1, 0 ,1]
        low = arr[i][j]
        possible = False
        
        for m in range(0, 8, 2):
            if (0 <= i+mv[m] < n) and (0 <= j+mv[m+1] < n):
                if low > arr[i+mv[m]][j+mv[m+1]]:
                    new_i, new_j = i+mv[m], j+mv[m+1]
                    low = arr[new_i][new_j]
                    possible = True
                    
        if possible:
            return 1 + road(new_i, new_j)
        else:
            return 1
    
    max_count = 0
    for i in range(n):                                          
        for j in range(n):
            max_count = max(max_count, road(i, j))
    
    print(f"#{test_case} {max_count}")
