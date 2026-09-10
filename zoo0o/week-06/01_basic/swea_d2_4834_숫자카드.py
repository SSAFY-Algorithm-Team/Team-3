# SWEA 4834. 숫자 카드
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZ9kDS86wCTHBITH&contestProbId=AWTLVouKpUgDFAVT&probBoxId=AZ9kDS86wCXHBITH&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+%EA%B8%B0%EB%B3%B8&problemBoxCnt=6

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = input()

    # 숫자 0~9의 등장 횟수 저장
    counts = [0] * 10

    # 1. 각 숫자의 개수 세기
    for card in cards:
        counts[int(card)] += 1

    # 2. 가장 많이 나온 숫자 찾기
    # 개수가 같으면 더 큰 숫자를 선택
    # max_card = 0
    #
    # for i in range(10):
    #     if counts[i] >= counts[max_card]:
    #         max_card = i

    max_card = max(range(10), key=lambda i: (counts[i], i))

    print(f'#{tc} {max_card} {counts[max_card]}')