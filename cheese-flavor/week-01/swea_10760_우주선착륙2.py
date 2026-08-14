# SWEA 10760. 우주선착륙2
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXSHJueab1oDFAQT
# 소요시간: 25분 / 시도: 1회

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    mv = [-1, 0, 1]  # [0, 0] 제외, 테이블 밖을 나가면 제외
    all_count = 0
    
    for i in range(n):
        for j in range(m):
            semi_count = 0
            
            for lm in mv:
                for rm in mv:
                    
                    if 0 <= i+lm < n and 0 <= j+rm < m:
                        if arr[i][j] > arr[i+lm][j+rm]:
                            semi_count += 1
                
            if semi_count >= 4:
                all_count += 1
            
    print(f"#{test_case} {all_count}")    