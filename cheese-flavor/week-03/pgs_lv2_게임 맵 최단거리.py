# 프로그래머스 Lv2. 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 소요시간: 40분 / 시도: 3회

#효율성 문제에서 틀려서 해당 파트 ai 도움을 받음

# 초기 코드
def solution(maps):
    
    # 0은 벽, 1은 경로 가능  / 경로 못가면 -1
    # 출발 (0,0) ?? (1,1) ??
    
    # 변수 정의
    answer, semi_count = 9999, 1 # 시작점을 포함해서 계산해서 1로 시작
    mv = [0, 1, 1, 0, 0, -1, -1, 0]  # 이동
    n, m = len(maps), len(maps[0])
    
    # 최소경로 찾기 알고리즘
    def ror(i, j):
        nonlocal answer, semi_count
        
        if i == (n-1) and j == (m-1):
            answer = min(answer, semi_count)
            return
        
        
        # 여기서는 그냥 초기화하는 형태로 가는게 가독성이 더 좋아보일꺼 같기두
        for v in range(0, 8, 2):
            if 0 <= i + mv[v] < n and 0 <= j + mv[v+1] < m :
                if maps[i + mv[v]][j + mv[v+1]] == 1 and not visited[i + mv[v]][j + mv[v+1]]:

                    #효율성 계산을 위해 가지치기 -> 근데 이거여도 부족하더라
                    if semi_count < answer: 
                        visited[i + mv[v]][j + mv[v+1]] = True
                        semi_count += 1
                    
                        ror(i + mv[v], j + mv[v+1])
                        visited[i + mv[v]][j + mv[v+1]] = False
                        semi_count -= 1

                    
    #visited = [[False] * n] *m -> 리스트 컴프리헨션 문제 (*m 참조하는 형태)
    visited = [[False]* m for _ in range(n)]
    visited[0][0] = True  # 시작점을 True로 초기화해야함
    ror(0, 0)
    
    
    # 경로 못찾아서 0일 경우
    if answer == 9999:
        answer = -1 
    
    return answer


# 효율성 목적으로 수정한 코드
from collections import deque

def solution(maps):

    # 변수 정의
    mv = [0, 1, 1, 0, 0, -1, -1, 0]  # 이동
    n, m = len(maps), len(maps[0])
    visited = [ [False] * m  for _ in range(n)]
    
    # deque를 이용해보자
    q = deque()
    q.append((0, 0, 1)) #((행, 열, 칸 수)) -> 튜플이니까
    visited[0][0] = True
    
    while q:
        i, j, count = q.popleft()
        
        if i == n-1 and j == m-1:
            return count
        
        for v in range(0, 8, 2):
            ni, nj = i+mv[v], j+mv[v+1]
            
            if 0 <= ni < n and 0 <= nj < m:
                if maps[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = True
                    q.append((ni, nj, count + 1))
                             
    return -1