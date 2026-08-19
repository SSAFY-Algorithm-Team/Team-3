# SWEA D3. 5656 벽돌 깨기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo
# 소요시간: 180분 / 시도: 3회
# 15:05

import sys
sys.stdin = open("sample_input.txt", "r")

def break_bricks(row, col, board):
    radius = board[row][col]

    board[row][col] = 0
    directions = [(0,-1),(0,1),(1,0),(-1,0)]

    for dr, dc in directions:
        for i in range(1,radius):
            nr = row + dr*i
            nc = col + dc*i
            if not(0<= nr < H and 0 <= nc < W):
                break
            if board[nr][nc] == 0:
                continue
            break_bricks(nr,nc,board)

def drop_bricks(board):
    for col in range(W):
        bricks = []
        # 해당 열에 있는 0이 아닌 벽돌을 리스트로 만듦
        for row in range(H):
            if board[row][col] != 0:
                bricks.append(board[row][col])
        # 해당 열을 비우고
        for row in range(H):
            board[row][col] = 0
        #가장 밑에서부터 채우기 시작
        row = H - 1
        while bricks:
            board[row][col] = bricks.pop()
            row -= 1

def count_brick(board):
    count = 0
    for row in range(H):
        for col in range(W):
            if board[row][col] != 0:
                count += 1
    return count

def dfs(depth, board):
    if depth == N:
        return count_brick(board)
    min_count = float('inf')
    found = False
    # 구슬 떨어트릴 열 탐색
    for col in range(W):
        #각 열마다 가장 위에 있는 행 찾기
        top_row=-1
        for row in range(H):
            if board[row][col] != 0:
                top_row = row
                break
        # 열이 비어있음
        if top_row == -1:
            continue
        found = True
        # 열을 선택할 때마다 현재 보드를 복사
        next_board = [line[:] for line in board]
        break_bricks(top_row, col, next_board)
        drop_bricks(next_board)
        
        next_count = dfs(depth+1, next_board)
        min_count = min(min_count, next_count)

    if not found:
        return 0
    return min_count

                
T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    init_board = [list(map(int, input().split())) for _ in range(H)]
    depth = 0
    result = dfs(depth, init_board)

    print(f'#{test_case} {result}')
