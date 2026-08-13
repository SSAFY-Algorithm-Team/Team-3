T = int(input())

for test_case in range(1, T+1):
    raw = input()
    cnt = 0

    for i in range(len(raw)):
        if raw[i] == '1':
            if cnt%2 == 0:
                cnt += 1
        elif raw[i] == '0':
            if cnt%2 == 1:
                cnt += 1

    print(f"#{test_case} {cnt}")