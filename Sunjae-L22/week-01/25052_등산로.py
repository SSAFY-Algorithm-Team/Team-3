T = int(input())


# 영역 정보와 시작점이 주어졌을 때, 최장경로를 구하는 함수
def cal_path_len(area, start_col, start_row):
    # 상하좌우
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    path_len = 1
    row, col = start_row, start_col
    real_row, real_col = 0, 0
    while True:
        # 현재 높이 
        now_height = area[col][row]

        # 다음 경로 있는지 여부 -> switch
        switch = False

        # 상하좌우 이동 가능한지
        for i in range(4):
            nrow = row + dir[i][1]
            ncol = col + dir[i][0]
            if 0 <= nrow < N and 0 <= ncol < N:
                # 4방향 중 가장 낮은 곳 찾기 위해
                if area[ncol][nrow] < now_height:
                    switch = True
                    now_height = area[ncol][nrow]
                    real_row = nrow
                    real_col = ncol

        if switch:
            col = real_col
            row = real_row
            path_len += 1
        else:
            break
    return path_len


for test_case in range(1, T+1):
    N = int(input())
    area = []
    for i in range(N):
        area.append(list(map(int, input().split())))

    # N제곱만큼 경로 존재, 그중 가장 긴 경로 찾기
    path_length = [0] * (N**2)
    for i in range(N):
        for j in range(N):
            path_length[i*N+j] = cal_path_len(area, i, j)
    print(f"#{test_case} {max(path_length)}")