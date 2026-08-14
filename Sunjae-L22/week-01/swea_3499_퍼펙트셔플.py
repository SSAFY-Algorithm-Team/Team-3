T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cards = list(input().split())

    # 짝수개일때
    if N % 2 == 0:
        first_deck = cards[ : int(N/2)]
        second_deck = cards[int(N/2) : ]
        new_deck = []
        for i in range(int(N/2)):
            new_deck.append(first_deck[i])
            new_deck.append(second_deck[i])

    else:
        first_deck = cards[ : int((N+1)/2)]
        second_deck = cards[int((N+1)/2) : ]
        new_deck = []
        for i in range(int((N+1)/2)-1):
            new_deck.append(first_deck[i])
            new_deck.append(second_deck[i])
        new_deck.append(first_deck[-1])

    print(f"#{test_case}", end = ' ')
    for card in new_deck:
        print(card, end = ' ')
    print()