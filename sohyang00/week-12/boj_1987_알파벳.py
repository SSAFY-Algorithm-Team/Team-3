import sys
sys.stdin = open("sample_input.txt", "r")

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c, cnt):
    max_count = cnt
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<= nr < R and 0<= nc < C:
            i = where(grid[nr][nc])
            if not visited[i]:
                visited[i] = True
                count = dfs(nr,nc, cnt+1)
                max_count = max(count, max_count)
                visited[i] = False
    return max_count


def where(arr):
    for i in range(26):
        if alpa[i] == arr:
            break
    return i

R, C = map(int, input().split())
grid = [list(map(str, input())) for _ in range(R)]
alpa = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
visited = [False]*26

i = where(grid[0][0])
visited[i] = True
result = dfs(0,0,1)
print(result)