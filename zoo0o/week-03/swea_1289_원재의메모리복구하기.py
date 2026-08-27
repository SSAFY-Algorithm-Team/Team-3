# SWEA 1289. 원재의 메모리 복구하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN
# 소요시간: 20분 / 시도: 2회

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input()))

    count, bit = 0, 0, 0

    while idx != len(arr):
        if arr[idx] != bit:
            bit ^= 1
            count += 1
        idx += 1

    print(f"#{tc} {count}")
