# 좌표 2배하는 게 너무 어려웠다. 그리고 벽 표시는 직사각형 내부, 테두리, 외부 이렇게 3가지로 나눠서 맵을 표시했는데, 이 부분도 살짝 헷갈렸다. 

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 좌표 2배 하기
    for idx_out, rec in enumerate(rectangle):
        for idx_in, r in enumerate(rec):
            rectangle[idx_out][idx_in] = 2*r
            
    # character, item 좌표도 2배 하기
    characterX, characterY, itemX, itemY = 2*characterX, 2*characterY, 2*itemX, 2*itemY
    
    # 벽, 방문 리스트
    wall = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[0 for _ in range(102)] for _ in range(102)]
    
    # 벽 표시하기
    for r in rectangle:
        x1, y1, x2, y2 = r[0], r[1],r[2],r[3]
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # 직사각형 내부면
                if x1 < i < x2 and y1 < j < y2:
                    wall[i][j] = 0
                # 다른 직사각형의 내부가 아니라면
                elif wall[i][j] != 0:
                    wall[i][j] = 1
    
    # character에서 BFS 시작
    min_cnt = float('inf')
    queue = deque([(characterX, characterY, 0)])
    visited[characterX][characterY] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    

    while queue:
        x, y, cnt = queue.popleft()
        # 아이템에 도달했다면
        if (x, y) == (itemX, itemY):
            min_cnt = min(cnt, min_cnt)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵 범위 검사
            if 0 <= nx < 102 and 0 <= ny < 102:
                # 테두리이고, 방문한 적이 없다면
                if wall[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    cnt += 1
                    queue.append((nx, ny, cnt))
    answer = min_cnt//2
    return answer