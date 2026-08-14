T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    pan = []

    for i in range(N):
        pan.append(list(input()))

    # 오목 달성여부
    fiveneck = "NO"

    # -> 판정
    for row in range(N):
        max_rock = 0    
        for col in range(N):
            if pan[row][col] == '.':
                max_rock = 0
            else:
                max_rock += 1
                if max_rock == 5:
                    fiveneck = "YES"

    # 아래방향 판정
    for col in range(N):
        max_rock = 0
        for row in range(N):
            if pan[row][col] == '.':
                max_rock = 0
            else:
                max_rock += 1
                if max_rock == 5:
                    fiveneck = "YES"

    # 좌상단우하단 화살표 판정
    for col in range(N):
        row = 0
        col = N - col
        max_rock = 0
        while 0 <= row < N and 0 <= col < N:
            if pan[row][col] == 'o':
                max_rock += 1
                if max_rock == 5:
                    fiveneck = "YES"
            else:
                max_rock = 0
            row += 1
            col += 1
    
    for row in range(N):
        col = 0
        max_rock = 0
        while 0 <= row < N and 0 <= col < N:
            if pan[row][col] == 'o':
                max_rock += 1
                if max_rock == 5:
                    fiveneck = "YES"
            else:
                max_rock = 0
            row += 1
            col += 1

    # 우상단좌하단 화살표 판정
    for col in range(N):
        row = 0
        max_rock = 0
        while 0 <= row < N and 0 <= col < N:
            if pan[row][col] == 'o':
                max_rock += 1
                if max_rock == 5:
                    fiveneck = "YES"
            else:
                max_rock = 0
            row += 1
            col -= 1
    
    for row in range(N):
        col = N-1
        max_rock = 0
        while 0 <= row < N and 0 <= col < N:
            if pan[row][col] == 'o':
                max_rock += 1
                if max_rock == 5:
                    fiveneck = "YES"
            else:
                max_rock = 0
            row += 1
            col -= 1


    print(f"#{test_case} {fiveneck}")