T = int(input())

for test_case in range(1, T+1):
    grass = list(input())
    ball = 0

    for i in range(len(grass)-1):
        if grass[i] == '(':
            if grass[i+1] == ')':
                ball += 1
            elif grass[i+1] == '|':
                ball += 1
        if grass[i] == '|':
            if grass[i+1] == ')':
                ball += 1

    print(f"#{test_case} {ball}")