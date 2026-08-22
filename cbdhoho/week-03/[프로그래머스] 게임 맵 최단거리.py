# 처음에 dfs로 풀었다가 코드 잘못 써서 gemini에게 물어봤더니, 이 문제는 dfs로 풀면 시간 초과가 날 확률이 높다고 하면서 bfs로 풀어야한다고 했음.
# bfs 알고리즘에 대해서 다 까먹어서 gemini의 코드를 사용함. 
# 맵 좌표마다 시작점에서 얼마나 걸리는지를 숫자 증가형식으로 처리함. -> 따로 리스트를 쓰거나 하지 않아도 됨.
# 만약 타겟 좌표 값이 1(벽 없음) 이상이면 해당 타켓 수를 반환하도록 함.

from collections import deque

def solution(maps):
    n = len(maps)       # 행 (높이)
    m = len(maps[0])    # 열 (너비)
    
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # Queue 생성 및 시작점 추가 (y, x)
    queue = deque([(0, 0)])
    
    while queue:
        y, x = queue.popleft()
        
        # 4방향 탐색
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # 맵 범위 내부이고, 지나갈 수 있는 길(1)인 경우
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                # 방문 처리 겸 거리 업데이트 (이전 칸 거리 + 1)
                maps[ny][nx] = maps[y][x] + 1
                queue.append((ny, nx))
                
    # 도착지점 값이 1이면 도달하지 못한 것 (-1 반환)
    target = maps[n-1][m-1]
    return target if target > 1 else -1