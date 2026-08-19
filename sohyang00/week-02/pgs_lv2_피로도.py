# 프로그래머스 Lv2. 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 소요시간: 60분 / 시도: 3회

# dfs, 백트래킹

def solution(k, dungeons):
    def dfs(k):
        nonlocal answer
        answer = max(answer, visited.count(True))
        for row in range(len(dungeons)):
            if not visited[row] and k >= dungeons[row][0]:
                visited[row] = True
                dfs(k-dungeons[row][1])
                visited[row] = False

    answer = -1
    visited = [False] * len(dungeons) # 던전 방문 여부 확인
    dfs(k)
    return answer