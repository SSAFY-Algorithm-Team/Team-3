T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    len_B = len(B_list)

    # B_list의 0번부터 M-1번까지 A에서 등장하는지 A를 훑으면서 체크
    check = 0

    for num in A_list:
        if num == B_list[check]:
            check += 1
        if check == M:
            break

    # 만약 길이 4짜리 B리스트의 4개 숫자가 순서대로 A 리스트에 있었다면, check는 4가 되어야함!
    answer = "NO"
    if check == M:
        answer = "YES"

    print(f"#{test_case} {answer}")