# SWEA 1926. 간단한 369게임
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq
# 소요시간: 25분 / 시도: 3회

n = int(input())
arr = ''

for i in range(1, n+1):
    if '3'  in str(i) or '6' in str(i) or '9' in str(i):
        for j in range(len(str(i))):
            if str(i)[j] in ['3', '6', '9']:
                arr += '-'
    else:
        arr += str(i)
        
    if i != n:
        arr += " "
        
print(arr)