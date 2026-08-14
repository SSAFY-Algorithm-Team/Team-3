# SWEA 1959. 두 개의 숫자열
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq
# 소요시간: 30분 / 시도: 8회

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    aj = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    max_arr = []
    if n < m:
        for i in range(m-n+1):
            res = 0
            for j in range(len(aj)):
                res += aj[j] * bj[i + j]
            max_arr.append(res)
    else:
        for i in range(n-m+1):
            res = 0
            for j in range(len(bj)):
                res += aj[i + j] * bj[j]
            max_arr.append(res)
    print(f"#{test_case} {max(max_arr)}")
