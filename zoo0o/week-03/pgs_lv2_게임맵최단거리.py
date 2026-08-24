# 프로그래머스 Lv2. 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# Solved with AI help

from collections import deque


from collections import deque


def solution(maps):
    # 맵의 행 개수
    n = len(maps)

    # 맵의 열 개수
    m = len(maps[0])

    # 상, 하, 좌, 우
    # r: row, 행
    # c: column, 열
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 방문 여부 + 시작점으로부터의 거리 저장
    # 0이면 아직 방문하지 않은 칸
    # 1 이상이면 방문한 칸이며, 값 자체가 이동 거리
    visited = [[0] * m for _ in range(n)]

    # 시작점은 첫 번째 칸부터 세므로 거리 1
    visited[0][0] = 1

    # BFS는 큐를 사용
    queue = deque()

    # 시작 위치 (행 0, 열 0) 저장
    queue.append((0, 0))

    # 큐에 탐색할 위치가 남아 있는 동안 반복
    while queue:
        # 가장 먼저 들어온 위치부터 꺼냄
        r, c = queue.popleft()

        # 현재 위치에서 상, 하, 좌, 우 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 다음 위치가 맵 범위 안인지 확인
            if 0 <= nr < n and 0 <= nc < m:

                # 길이고, 아직 방문하지 않은 칸만 이동
                if maps[nr][nc] == 1 and visited[nr][nc] == 0:

                    # 현재 거리 + 1을 다음 칸에 저장
                    visited[nr][nc] = visited[r][c] + 1

                    # 다음에 탐색할 위치를 큐에 추가
                    queue.append((nr, nc))

    # 도착점을 방문하지 못한 경우
    if visited[n - 1][m - 1] == 0:
        return -1

    # 도착점까지의 최단거리 반환
    return visited[n - 1][m - 1]
