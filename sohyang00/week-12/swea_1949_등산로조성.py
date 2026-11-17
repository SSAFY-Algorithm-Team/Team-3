import sys
sys.stdin = open("sample_input.txt","r")
from collections import deque

def find_route(r,c):
    d, broken = dist[r][c]
    best = d
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0<=nr<N and 0<=nc<N and dist[nr][nc][0] == -1:
            if grid[nr][nc] < grid[r][c]: #다음에 갈 곳이 낮으면 이동
                dist[nr][nc] = (dist[r][c][0]+1, dist[r][c][1])
                result = find_route(nr,nc)
                best = max(best, result)
                dist[nr][nc] = (-1, 0)
            elif broken == 0 and grid[nr][nc] - K < grid[r][c]: 
                original = grid[nr][nc]
                grid[nr][nc] = grid[r][c] - 1
                dist[nr][nc] = (d+1, 1)
                result = find_route(nr,nc)
                best = max(best, result)
                dist[nr][nc] = (-1,0)
                grid[nr][nc] = original
    return best

T = int(input())

dr = [-1,1,0,0]
dc = [0,0,-1,1]

for testCase in range(1, T+1):
    N, K = map(int, input().split()) # K가 공사 가능 깊이였음...;;
    grid = [list(map(int, input().split())) for _ in range(N)]

    #가장 높은 곳 높이 찾기
    max_h = 0    
    tops = []
    for r in range(N):
        for c in range(N):
            if max_h < grid[r][c]:
                max_h = grid[r][c]

    #높은 곳 좌표 찾기
    for r in range(N):
        for c in range(N):
            if grid[r][c] == max_h:
                tops.append((r,c))

    max_route = 0

    # 각 봉우리마다 최대 등산로의 길이를 탐색
    for tr, tc in tops:
        dist = [[(-1,0)]*N for _ in range(N)] #거리, 깎은 여부
        dist[tr][tc] = (1,0)
        route = 0
        route = find_route(tr,tc)

        max_route = max(route, max_route)
    print(f'#{testCase} {max_route}')