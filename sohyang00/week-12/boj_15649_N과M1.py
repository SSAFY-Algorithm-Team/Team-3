import sys
sys.stdin = open("sample_input.txt","r")
from itertools import combinations

def dfs(perm, level):
    if level == M: 
        return [perm.copy()]
    
    rows = [] 
    for j in range(1, N+1):
        if not visited[j]:
            visited[j] = True
            perm.append(j)

            rows.extend(dfs(perm, level+1)) # extend: 리스트로 값 받음. append: 문자열 뒤에 문자 하나를 덧붙임

            visited[j] = False
            perm.pop()

    return rows

N,M= map(int,input().split())
numbers = [i for i in range(1,N+1)]
result = []
# 순열
if M == 1:
    for arr in range(1,N+1):
        print(arr)
else: 
    for i in numbers:
        permu = []
        visited = [False]*(N+1)
        visited[i] = True
        permu.append(i)
        result.extend(dfs(permu, 1))

    for row in result:
        print(*row)


    
