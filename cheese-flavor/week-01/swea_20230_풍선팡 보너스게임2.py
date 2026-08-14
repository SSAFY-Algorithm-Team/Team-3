# SWEA 20230. 풍선팡 보너스게임2
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AY3FFOTaN7EDFAXh
# 소요시간: 15분 / 시도: 1회

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
        
    max_score = 0
    
    for i in range(n):
        for j in range(n):
            score = (sum(arr[i]) - arr[i][j])
            
            for k in range(n):
                score += arr[k][j]
                
            if score > max_score:
                max_score = score
            
    print(f"#{test_case} {max_score}") 