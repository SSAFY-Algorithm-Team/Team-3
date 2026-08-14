T = int(input())


def ClassifyFruit(weight_list, k1, k2):
    economy, standard, premium = 0, 0, 0
    k1 += 0.5
    k2 += 0.5

    for weight in weight_list:
        if weight < k1:
            economy += 1
        elif k1 <= weight < k2:
            standard += 1
        else:
            premium += 1

    return economy, standard, premium


for test_case in range(1, T+1):
    N, low, high = map(int, input().split())
    fruit_weights = list(map(int, input().split()))

    sorted_fruit_weights = sorted(fruit_weights)
    answer = N+1

    for k1 in range(N):
        for k2 in range(k1, N):
            economy_n, standard_n, premium_n = ClassifyFruit(fruit_weights, sorted_fruit_weights[k1], sorted_fruit_weights[k2]-1)

            max_n = max(economy_n, standard_n, premium_n)
            min_n = min(economy_n, standard_n, premium_n)

            if low <= min_n and high >= max_n:
                answer = min(answer, max_n - min_n)

    if answer == N+1:
        print(f"#{test_case} -1")
    else:
        print(f"#{test_case} {answer}")