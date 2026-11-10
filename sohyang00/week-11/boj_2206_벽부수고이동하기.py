import sys
sys.stdin = open("sample_input.txt","r")
from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]
n, m = map(int, input().split())
grid = [list(map(int, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def bfs():
    q = deque([(0,0,1,0)])
    while q:
        r,c,cost,broken = q.popleft()
        if r == n -1 and c == m-1:
            return cost

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
                if grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr,nc,cost+1,broken))
                elif grid[nr][nc] == 1 and broken == 0:
                    visited[nr][nc] = True
                    q.append((nr,nc,cost+1,1))
    return -1
        
print(bfs())




