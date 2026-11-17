import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

def isRun(cards, stat):
    # print(cards)
    if 3 in cards:
        return 1
    else: 
        return stat

def isTriple(cards, stat):
    for i in range(8):
        # print(i, cards[i], i+1, cards[i+1], i+2, cards[i+2])
        if cards[i] != 0 and cards[i+1] != 0 and cards[i+2] != 0:
            return 1
    return stat

for testCase in range(1, T+1):
    arr = list(map(int, input().split()))
    p1_card = [0] * 10
    p2_card = [0] * 10
    p1_status, p2_status = 0, 0
    result = 0

    for i in range(0,len(arr),2):
        p1_card[arr[i]] += 1
        p2_card[arr[i+1]] += 1
        # 0 2 4 6 8 10 12
        if i >= 4:
            p1_status= isRun(p1_card, p1_status)
            p1_status = isTriple(p1_card, p1_status)
            p2_status = isRun(p2_card, p2_status)
            p2_status = isTriple(p2_card, p2_status)

            if p1_status == 1 and p2_status == 1:
                result = 1
                break
            elif p1_status == 1 and p2_status == 0:
                result = 1
                break
            elif p1_status == 0 and p2_status == 1:
                result = 2
                break

    if p1_status == 0 and p2_status == 0: 
        result = 0
    print(f'#{testCase} {result}')