T = int(input())
 
def dfs(x,y,length):
 
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
 
    neighbor = []
 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 좌표 범위
        if 0 <= nx < N and 0 <= ny < N:
            # 현재 좌표보다 더 낮으면
            if mat[x][y] > mat[nx][ny]:
                # 주변 좌표들이랑 비교 list
                neighbor.append([nx, ny, mat[nx][ny]])
 
    if neighbor:
        neighbor.sort(key = lambda x: x[2])
 
        min_x = neighbor[0][0]
        min_y = neighbor[0][1]
        return dfs(min_x, min_y, length+1)
    else:
        return length
 
for tc in range(1, T+1):
    N = int(input())
    max_length = 0
 
    mat = [list(map(int, input().split())) for _ in range(N)]
 
    for x in range(N):
        for y in range(N):
            length = dfs(x, y, 1)
            if length > max_length:
                max_length = length
    print(f"#{tc} {max_length}")