# SWEA 26059. 과일 등급 분류
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZwl9ifa3dLHBIT3
# 소요시간: 50분 / 시도: 1회

T = int(input())

for test_case in range(1, T + 1):
    n, lo, hi = map(int, input().split())
    weights = list(map(int, input().split()))

    diff_min = float('inf')

    weights.sort()

    for i in range(n - 1):
        if weights[i] != weights[i + 1]:
            k1 = i + 1
            for j in range(i + 1, n - 1):
                if weights[j] != weights[j + 1]:
                    k2 = j + 1
                    low = k1
                    mid = k2 - k1
                    high = n - k2
                    if low < lo or mid < lo or high < lo or low > hi or mid > hi or high > hi:
                        continue
                    score = max(low, mid, high) - min(low, mid, high)
                    if score < diff_min:
                        diff_min = score

    if diff_min == float('inf'):
        diff_min = -1

    print(f"#{test_case} {diff_min}")
