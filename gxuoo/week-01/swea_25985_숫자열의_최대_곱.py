# SWEA 25985. 숫자열의 최대 곱
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZvmEUAqG6LHBIQE
# 소요시간: 20분 / 시도: 1회

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = []
    for _ in range(N-1):
        b.insert(0, 0)
    for _ in range(N-1):
        b.append(0)
    for i in range(M + N - 1):
        total = 0
        for j in range(N):
            total += a[j] * b[i+j]
        res.append(total)
                
    max_sum = max(res)
    print(f"#{test_case} {max_sum}")
