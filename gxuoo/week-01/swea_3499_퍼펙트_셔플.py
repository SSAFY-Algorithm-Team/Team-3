# SWEA 3499. 퍼펙트 셔플
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW
# 소요시간: 20분 / 시도: 1회

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(str, input().split()))
    if N % 2 == 0:
        left = arr[:(N // 2)]
        right = arr[(N // 2):]
    else:
        left = arr[:(N // 2 + 1)]
        right = arr[(N // 2 + 1):]

    print(f"#{test_case}", end=' ')
    while True:
        print(left.pop(0), end=' ')
        if len(right) <= 0:
            break
        print(right.pop(0), end=' ')
        if len(left) <= 0 and len(right) <= 0:
            break
    print()
