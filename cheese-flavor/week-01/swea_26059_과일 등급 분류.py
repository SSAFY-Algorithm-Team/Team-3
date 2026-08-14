# SWEA 26059. 과일 등급 분류
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZwl9ifa3dLHBIT3
# 소요시간: 70분 / 시도: 1회

from itertools import groupby

T = int(input())
for test_case in range(1, T + 1):
    n, lo, hi = map(int, input().split())
    fruit = sorted(list(map(int, input().split())))
    
    groups = []
    for val, g in groupby(fruit):
        groups.append((val, len(list(g))))
    
    d = len(groups)
    result = float('inf')
    
    if d < 3:
        print(f"#{test_case} -1")
        continue
        
    for cut1 in range(1, d):
        for cut2 in range(cut1 + 1, d):
            
            economy = 0
            for i in range(0, cut1):
                economy += groups[i][1]
                
            standard = 0
            for i in range(cut1, cut2):
                standard += groups[i][1]
                
            premium = 0
            for i in range(cut2, d):
                premium += groups[i][1]
                
            if lo <= economy <= hi and lo <= standard <= hi and lo <= premium <= hi:
                diff = max(economy, standard, premium) - min(economy, standard, premium)
                result = min(result, diff)
                
    if result == float('inf'):
        print(f"#{test_case} -1")
    else:
        print(f"#{test_case} {result}")
