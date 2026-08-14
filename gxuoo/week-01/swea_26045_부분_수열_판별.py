# SWEA 26045. 부분 수열 판별
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZwe0FZaG1bHBIPa
# 소요시간: 35분 / 시도: 3회

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    flag = True
    index = 0
    for i in range(M):
        arr = a[index::]
        if b[i] in arr:
            sub_index = arr.index(b[i]) 
            index += sub_index + 1
        else:
            flag = False
    if flag:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")
