T = int(input())


def ballon_pang(ballons, row, col, N):
    # row, col 풍선을 터뜨렸을 때 얻는 점수 반환하는 함수 구현
    score = 0

    # 열방향 모두 더하기
    for r in range(N):
        score += ballons[r][col]

    # 행방향 모두 더하기
    for c in range(N):
        score += ballons[row][c]

    # 겹친 가운데 점 한번 빼주기
    score -= ballons[row][col]

    return score


for test_case in range(1, T+1):
    N = int(input())
    ballons = []

    for _ in range(N):
        ballons.append(list(map(int, input().split())))

    scores = []

    for row in range(N):
        for col in range(N):
            scores.append(ballon_pang(ballons, row, col, N))

    print(f"#{test_case} {max(scores)}")