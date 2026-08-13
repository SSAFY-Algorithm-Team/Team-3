T = int(input())


# 파리지도, 분사점, 세기를 입력받아 + 모양으로 스프레이를 뿌렸을때 퇴치되는 파리의 수를 반환
def spray_plus(fly_map, N, row, col, M):
    dead_fly = fly_map[row][col]
    # 상하좌우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for direction in directions:
        for power in range(1, M):
            next_row = row + power * direction[0]
            next_col = col + power * direction[1]

            if (0 <= next_row < N) and (0 <= next_col < N):
                dead_fly += fly_map[next_row][next_col]

    return dead_fly

# 파리지도, 분사점, 세기를 입력받아 x 모양으로 스프레이를 뿌렸을때 퇴치되는 파리의 수를 반환
def spray_multi(fly_map, N, row, col, M):
    dead_fly = fly_map[row][col]
    # 대각선 방향들
    directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    
    for direction in directions:
        for power in range(1, M):
            next_row = row + power * direction[0]
            next_col = col + power * direction[1]

            if (0 <= next_row < N) and (0 <= next_col < N):
                dead_fly += fly_map[next_row][next_col]

    return dead_fly



for test_case in range(1, T+1):
    N, M = map(int, input().split())
    fly_map = [0] * N
    
    for i in range(N):
        fly_map[i] = list(map(int, input().split()))

    able_fly_kill = []

    for row in range(N):
        for col in range(N):
            able_fly_kill.append(spray_plus(fly_map, N, row, col, M))
            able_fly_kill.append(spray_multi(fly_map, N, row, col, M))

    print(f"#{test_case} {max(able_fly_kill)}")