# SWEA D3. 5656 벽돌 깨기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo
# 소요시간: 60분 / 시도: 3회
# 15:05

#각 열마다 가장 위에 있는 벽돌의 위치랑 정보를 저장해두는 게 필요할까 ?? ...
#ㄴㄴ 걍 완탐 돌리는 게 낫겟다 
#재귀? 
# 근데 터트리고 나서 맵 어케 함? 

# 깨야할 벽돌 찾는 로직
# 벽돌 찾았으면 주위 벽돌 깨고 깨졋음 한칸 씩 내리는 로직
# 0으로 다 바꾸고.. 열 탐색해서 행+1이 0이면 둘이 바꿔주기


import sys
sys.stdin = open("input.txt", "r")

def break_bricks(row, col, board):
    radius = board[row][col]

    board[row][col] = 0
    directions = [(0,-1),(0,1),(0,1)]

    for dr, dc in directions:
        for i in range(radius):
            nr = row + dr*i
            nc = col + dc*i
            if 0<= nr < W and 0 <= nc < H:
                board[nr][nc] = 0

    return board

def drop_bricks(board):
    for col in range(H):
        for row in range(W):
            if board[row][col] >= 1 and board[row+1][col] == 0:
                board[row+1][col] = board[row][col]
                board[row][col] = 0 
                break
    return board

def count_brick(board):
    count = 0
    for row in range(W):
        for col in range(H):
            if board[row][col] >= 1:
                count += 1
    return count

def dfs():
    board = init_board
    min_count = 0
    n_count = 0
    for col in range(H):
        for row in range(W):
            if board[row][col] >= 1:
                board = break_bricks(row, col, board)
                board = drop_bricks(board)
                n_count += 1
                if n_count == 3:
                    cur_count = count_brick
                    min_count = min(min_count, cur_count)
    return min_count

                


T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    init_board = [list(map(int, input().split())) for _ in range(H)]

    result = dfs()

    print(f'#{{result}}')
