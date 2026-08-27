# 프로그래머스 Lv2. 게임맵최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 소요시간: 20분 / 시도: 1회

from collections import deque

def solution(maps):

    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((0, 0))
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1

    while q:
        now_r, now_c = q.popleft()
        if (now_r, now_c) == (n-1, m-1):
            return dist[now_r][now_c]
        for d in range(4):
            nr, nc = now_r + dr[d], now_c + dc[d]
            # 다음 탐색 칸이 범위 안에 있고, 아직 안가서 거리행렬이 비어있고, 길일 때 q에 append
            if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1 and maps[nr][nc] == 1:
                q.append((nr, nc))
                dist[nr][nc] = dist[now_r][now_c] + 1

    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))