T = int(input())


def is_it_increasing(a, b):
    tgt = str(a * b)
    flag = True

    for i in range(1, len(tgt)):
        if int(tgt[i]) < int(tgt[i-1]):
            flag = False

    if flag:
        return int(tgt)
    else:
        return -1


for test_case in range(1, T+1):
    N = int(input())
    A_list = list(map(int, input().split()))
    answer = -1

    for i in range(N):
        for j in range(i+1, N):
            answer = max(answer, is_it_increasing(A_list[i], A_list[j]))

    print(f"#{test_case} {answer}")