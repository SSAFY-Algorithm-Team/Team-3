T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    # 농장 내 농작물 가치행렬
    farm = []
    for i in range(N):
        farm.append(list(input()))

    # 수익 계산 
    profit = 0
    middle_column = (N-1) // 2

    if N == 1:
        profit = int(farm[0][middle_column])
    else:
        profit = int(farm[0][middle_column]) + int(farm[N-1][middle_column])

    for row in range(1, N-1):
        # 가운데 더하고, 앞뒤로 row칸만큼 이동하면서 더해주기
        profit += int(farm[row][middle_column])
        n_row = row
        if row > middle_column:
            n_row = N - 1 - row

        # 앞
        for front in range(1, n_row+1):
            profit += int(farm[row][middle_column-front])

        # 뒤
        for back in range(1, n_row+1):
            profit += int(farm[row][middle_column+back])

    print(f"#{test_case} {profit}")