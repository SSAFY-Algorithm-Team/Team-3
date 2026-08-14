T = int(input())


def able_take_picture(height_map, N, M, row, col):
    now_height = height_map[row][col]
    cnt = 0
    # 상부터 시계방향으로 8방향 이동 
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for direction in directions:
        next_row = row + direction[0]
        next_col = col + direction[1]
        if (0 <= next_row < N) and (0 <= next_col < M):
            next_height = height_map[next_row][next_col]
            if now_height > next_height:
                cnt += 1

    if cnt >= 4:
        return True
    else:
        return False



for test_case in range(1, T+1):
    N, M = map(int, input().split())
    height_map = [0] * N

    for i in range(N):
        height_map[i] = list(map(int, input().split()))

    candidate = 0
    for i in range(N):
        for j in range(M):
            if able_take_picture(height_map, N, M, i, j):
                candidate += 1

    print(f"#{test_case} {candidate}")