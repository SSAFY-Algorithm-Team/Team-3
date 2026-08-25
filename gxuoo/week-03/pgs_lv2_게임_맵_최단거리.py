# 프로그래머스 Lv2. 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 소요시간: 90분 / 시도: 1회

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    distance = [[0] * m for _ in range(n)]

    queue = deque()
    queue.append((0, 0))
    distance[0][0] = 1
    
    while queue:
        cur_row, cur_col = queue.popleft()
        
        if cur_row == n - 1 and cur_col == m - 1:
            return distance[cur_row][cur_col]
        
        for row_delta, col_delta in directions:
            next_row = cur_row + row_delta
            next_col = cur_col + col_delta
            
            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= m:
                continue
                            
            if not maps[next_row][next_col]:
                continue
                
            if distance[next_row][next_col]:
                continue         
        
            distance[next_row][next_col] = distance[cur_row][cur_col] + 1
            queue.append((next_row, next_col))
                   
    return -1
