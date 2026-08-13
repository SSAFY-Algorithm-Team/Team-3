T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    len_a = len(A)
    len_b = len(B)
    longer = max(len_a, len_b)
    shorter = min(len_a, len_b)

    if len_a >= len_b:
        longer_list = A
        shorter_list = B
    else:
        longer_list = B
        shorter_list = A

    # 두 리스트의 길이 차이 + 1만큼 이동하며 곱을 모두 구한 뒤 비교한다. 
    mul_list = []
    window = longer - shorter

    for i in range(window + 1):
        res = 0
        for j in range(shorter):
            res += shorter_list[j] * longer_list[j+i]
        mul_list.append(res)

    print(f"#{test_case} {max(mul_list)}")