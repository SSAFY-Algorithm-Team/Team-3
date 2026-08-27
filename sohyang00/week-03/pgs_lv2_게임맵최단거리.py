# 프로그래머스 Lv2. 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

# dfs 누적합, 현재 위치까지의 거리를 기록
# 만약 끝까지 탐색해도 갈 수 있는 곳이 없다면? 다른 방향으로 갈 수 있을 때까지 리턴

from collections import deque
import sys
input = sys.stdin.readline

directions = [
    (0,1), 
    (0,-1), 
    (1,0), 
    (-1,0), 
]

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    distance = [[-1] * M for _ in range(N)]
    distance[0][0] = 1

    queue = deque([(0, 0)])
    while queue:
        row, col = queue.popleft()
        if row == N -1 and col == M -1: 
            return distance[row][col]
        for dr, dc in directions:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < N and 0 <= nc < M : 
                if maps[nr][nc] == 1 and distance[nr][nc] == -1:
                    distance[nr][nc] = distance[row][col]+1
                    queue.append((nr, nc))
    return -1

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
