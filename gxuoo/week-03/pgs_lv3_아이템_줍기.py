# 프로그래머스 Lv3. 아이템 줍기 (코어 문제)
# https://school.programmers.co.kr/learn/courses/30/lessons/87694
# 소요시간: 120분 / 시도: 1회

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    SIZE = 102
    board = [[0] * SIZE for _ in range(SIZE)]
    visited = [[False] * SIZE for _ in range(SIZE)]

    # 모든 사각형의 테두리를 1로
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for x in range(x1, x2 + 1):
            board[x][y1] = 1
            board[x][y2] = 1
        for y in range(y1, y2 + 1):
            board[x1][y] = 1
            board[x2][y] = 1

    # 모든 사각형의 내부를 0으로 (테두리는 건드리지 않음)
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 0

    # TODO: (characterX*2, characterY*2)에서 시작하는 BFS
    #  - board[nx][ny] == 1 인 칸으로만 이동
    #  - (itemX*2, itemY*2)에 도달하면 거리 return
    #  - 마지막에 // 2 잊지 말기
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    q = deque([(characterX * 2, characterY * 2, 0)])
    visited[characterX * 2][characterY * 2] = True
    
    while q:
        cur_x, cur_y, dist = q.popleft()
        if cur_x == itemX * 2 and cur_y == itemY * 2:
            return dist // 2
    
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
        
            if next_x < 0 or next_x >= SIZE or next_y < 0 or next_y >= SIZE:
                continue
        
            if not board[next_x][next_y] or visited[next_x][next_y]:
                continue
        
            visited[next_x][next_y] = True
            q.append((next_x, next_y, dist + 1))
