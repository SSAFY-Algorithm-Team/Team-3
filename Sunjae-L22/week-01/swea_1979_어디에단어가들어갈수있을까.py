T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = []

    for i in range(N):
        puzzle.append(list(map(int, input().split())))

    answer = 0

    # 가로 방향 가능한지 체크
    for row in range(N):
        cnt = []
        tmp = 0
        # 연속으로 등장해야만. 검은색이 나오면 cnt를 0으로 초기화
        for col in range(N):
            if puzzle[row][col] == 1:
                tmp += 1
                if col == N-1:
                    cnt.append(tmp)
            if puzzle[row][col] == 0:
                cnt.append(tmp)
                tmp = 0
        for num in cnt:
            if num == K:
                answer += 1

    # 세로 방향 가능한지 체크
    for col in range(N):
        cnt = []
        tmp = 0
        for row in range(N):
            if puzzle[row][col] == 1:
                tmp += 1
                if row == N-1:
                    cnt.append(tmp)
            if puzzle[row][col] == 0:
                cnt.append(tmp)
                tmp = 0
        for num in cnt:
            if num == K:
                answer += 1

    print(f"#{test_case} {answer}")