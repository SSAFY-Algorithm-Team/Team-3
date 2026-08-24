# 프로그래머스 Lv2. 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

# dfs 누적합, 현재 위치까지의 거리를 기록
# 만약 끝까지 탐색해도 갈 수 있는 곳이 없다면? 다른 방향으로 갈 수 있을 때까지 리턴

directions = [
    (0,1), 
    (0,-1), 
    (1,0), 
    (-1,0), 
]

def solution(maps):
    answer = -1
    min_length = float('inf')
    N = len(maps)
    M = len(maps[0])
    chk = [[False] * N for _ in range(M)]

    def dfs(row, col, length):
        nonlocal min_length, answer
        if row == N-1 and col == M-1:
            min_length = min(length, min_length)
            answer = min_length
            return

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            if 0<=nr<N and 0<= nc<M and maps[nr][nc] == 1 and not chk[nr][nc]:
                chk[nr][nc] = True
                dfs(nr, nc, length+1)
                chk[nr][nc] = False

    dfs(0,0,1)
    print(f'{answer}')
    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
