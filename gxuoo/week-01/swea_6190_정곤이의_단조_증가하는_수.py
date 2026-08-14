# SWEA 6190. 정곤이의 단조 증가하는 수
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWcPjEuKAFgDFAU4
# 소요시간: 1시간 이상 / 시도: 4회

def is_mono(x):
    s = str(x)
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = -1

    for i in range(n - 1):
        for j in range(i + 1, n):
            m = arr[i] * arr[j]
            if m > result and is_mono(m):
                result = m

    print(f"#{test_case} {result}")
