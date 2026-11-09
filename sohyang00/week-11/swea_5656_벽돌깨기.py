import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def crush(row, col, idx_board):
    power = idx_board[row][col]
    if power == 1: 
        idx_board[row][col] = 0
        return idx_board 
    elif power == 0: 
        return idx_board 
    else: 
        # 상하좌우를 터트려야함
        # 얼마나? 벽돌에 적힌 값만큼
        # 근데 그 값을 dfs에 같이 보낼건지, 아니면 while로 해결이 가능한지 모르겠음
        for dist in range(1, power):
            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]

                if 0 <= nr < H and 0 <= nc < W: 
                    if idx_board[row][col] != 0:
                        crush(nr,nc,idx_board)
    return idx_board

def gravity(idx_board):
    #행마다 확인하면 될 거 같은데...
    #0열의 현재 행이 0이고 위에 1이 있으면 현재를 1로 바꾸고, 위를 0으로 바꾼다.
    #근데 중간에 0이 두개면 어쩔건데... 이중 for? 
    for col in range(W-1,-1,-1):
        write = H-1
        for row in range(H-1,-1,-1):
            if idx_board[row][col] != 0:
                brick = idx_board[row][col]
                idx_board[row][col] = 0
                idx_board[write][col] = brick
                write -= 1

    return idx_board



def sol(idx, board):
    idx_board = board
    
    # c idx열에서 r행에 벽돌이 있을때까지 내려감
    for row in range(H): 
        if board[row][idx] == 0: 
            continue
        else:
            break

    idx_board = crush(row, idx, idx_board)
    # 터트림
    # 연쇄폭발도 일어남
    idx_board = gravity(idx_board)
    # 중력으로 떨어짐

    for i in range(W):
        for j in range(H):
            if idx_board[i][j] != 0:
                cnt += 1

    return cnt # 남은 벽돌의 개수


for testCase in range(1,T+1):
    N, W, H = map(int, input().split())
    board = [list(map(int,input().split())) for _ in range(H)]
    print(board)

    #구슬은 모든 위치에서 쏠 수 있다. 0~8번까지
    #구슬이 명중한 벽돌은 상하좌우 벽돌숫자-1 칸이 같이 제거된다. 
    #연쇄 충돌이 일어날 수 있다.
    #빈 공간이 있다면 벽돌은 밑으로 떨어짐
    #남은 벽돌의 개수를 구하라

    for idx in range(W):
        min_total = min(sol(idx, board), min_total)

