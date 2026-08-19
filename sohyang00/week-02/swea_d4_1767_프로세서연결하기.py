# SWEA D4. 1767 프로세서 연결하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf
# 소요시간: 180분 / 시도: 3회
# 10:18

# 코어 최대 12개
# 각 코어 당 상하좌우 4번씩 다 탐색해도 12*4 = 48번
# 보드 12*12 = 144 
# 대충 150*50 = 7500
# 전선 길이 최소 구하기 
# 파이썬 8초 8천만 연산 -> tc 60개 -> 1개당 약 100만 연산
# 완탐해도 될 듯
# 1. 최대한 많은 코어 2. 전선 길이의 합이 최소

# 이것도 그냥 하나하나 다 해서 어떤 경우가 코어가 젤 많고, 전선길이가 짧은지 봐야할 듯
# 그러면 dfs에 넘겨야하는게 몇번째 코어인지를 봐야함? 


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
             
# 코어 선택
def dfs(idx, connected, wire_length):
    global max_connected, min_wire

    # 종료 조건
    # 현재 연결된 코어 수가 프로세서에 있는 코어 수와 같으면
    if idx == len(cores): 
        if connected > max_connected:
            max_connected = connected
            min_wire = wire_length
        elif connected == max_connected:
            min_wire = min(min_wire, wire_length)
        return
    
    row, col = cores[idx]

    for dr, dc in directions:
        path = []
        nr = row + dr
        nc = col + dc

        while 0 <= nr < N and 0<=nc<N:
            if board[nr][nc] != 0:
                path = []
                break
            path.append((nr,nc))
            nr += dr
            nc += dc
        if path:
            for nr, nc in path: 
                board[nr][nc] = 2
            dfs(idx+1, connected+1, wire_length+len(path))
            for nr, nc in path:
                board[nr][nc] = 0

    dfs(idx+1, connected,wire_length)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cores = [
        (r, c) 
        for r in range(1, N-1) 
        for c in range(1, N-1)
        if board[r][c] == 1]
    min_wire = float('inf')
    max_connected = 0
    dfs(0, 0, 0)

    print(f'#{test_case} {min_wire}')

