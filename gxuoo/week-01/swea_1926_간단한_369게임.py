# SWEA 1926. 간단한 369게임
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq
# 소요시간: 15분 / 시도: 2회

T = int(input())
for test_case in range(1, T + 1):
    s = str(test_case)
    count = 0

    for char in s:
        if char in '3' or char in '6' or char in '9':
            count += 1
    if count == 0:
        print(s, end='')
    else:
        print('-' * count, end='')
    print(end=' ')
