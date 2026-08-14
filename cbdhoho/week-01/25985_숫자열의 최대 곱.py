T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # B is long arr
    if len(A) > len(B):
        temp = A
        A = B
        B = temp

    for _ in range(len(A)-1):
        B.insert(0, 0)
        B.append(0)

    max_sum = float('-inf')

    for i in range(len(B)-len(A)+1):
        sum = 0
        for j in range(len(A)):
            sum += A[j]*B[i+j]
        if sum > max_sum:
            max_sum = sum
    print(f"#{tc} {max_sum}")