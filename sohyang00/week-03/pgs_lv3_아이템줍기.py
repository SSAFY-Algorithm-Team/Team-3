# 프로그래머스 Lv3. 아이템 줍기
# https://school.programmers.co.kr/learn/courses/30/lessons/87694

from collections import deque

directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    board = [[0] * 102 for _ in range(102)]
    visited = [[False] * 102 for _ in range(102)]
    start_x = characterX * 2
    start_y = characterY * 2
    target_x = itemX * 2
    target_y = itemY * 2
    queue = deque([(start_x,start_y,0)])
    visited[start_y][start_x] = True

    for x1,y1,x2,y2 in rectangle:
        x1*=2
        y1*=2
        x2*=2
        y2*=2
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                board[y][x] = 1

    for x1,y1,x2,y2 in rectangle:
        x1*=2
        y1*=2
        x2*=2
        y2*=2
        for y in range(y1+1, y2):
            for x in range(x1+1, x2):
                board[y][x] = 0

    while queue:
        x, y, distance = queue.popleft()

        if x == target_x and y == target_y:
            return distance // 2

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0<=nx<102 and 0<=ny<102:
                if board[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx,ny, distance+1))
    
    return 0