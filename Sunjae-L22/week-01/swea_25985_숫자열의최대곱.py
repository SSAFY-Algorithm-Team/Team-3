T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if len(A) > len(B):
        tmp = A
        A = B
        B = tmp
        tmp = N
        N = M
        M = tmp
    muls = []

    # 1 ~ N-1 : A의 오른쪽 부분과 B의 왼쪽 일부가 곱해짐
    for i in range(1, N):
        mul = 0

        for j in range(i):
            mul += A[N-i+j] * B[j]
        muls.append(mul)

    # N ~ M : N 전체가 곱해짐
    for i in range(M-N+1):
        mul = 0

        for j in range(N):
            mul += A[j] * B[i+j]
        muls.append(mul)

    # M+1 ~ M+N-1 : A의 왼쪽 부분과 B의 오른쪽 일부가 곱해짐
    for i in range(1, N):
        mul = 0

        for j in range(i):
            mul += A[j] * B[M-i+j]
        muls.append(mul)

    print(f"#{test_case} {max(muls)}")