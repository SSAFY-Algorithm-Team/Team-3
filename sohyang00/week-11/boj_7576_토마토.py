import sys
sys.stdin = open("sample_input.txt", "r")

from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(arr):
    q = deque(arr)
    while q:
        cr,cc = q.popleft()

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            if 0<=nr<m and 0<=nc<n:
                if not visited[nr][nc] and grid[nr][nc] != -1:
                    visited[nr][nc] = True
                    grid[nr][nc] = grid[cr][cc] + 1
                    q.append((nr,nc))

    minDay = 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 0:
                return -1
            elif grid[row][col] > minDay:
                minDay = grid[row][col]
    return minDay - 1

        

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
visited = [[False]*n for _ in range(m)]
cnt = 0
isTrue = []
for r in range(m):
    for c in range(n):
        if grid[r][c] == 1:
            cnt += 1
            isTrue.append((r,c))
            visited[r][c]=True 

if cnt == n*m:
    print(0)
else: 
    result = bfs(isTrue)
    print(result)

