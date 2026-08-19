# 프로그래머스 Lv2. 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 소요시간: 6O분 / 시도: 1회

def solution(k, dungeons):
    visited = [False for _ in range(len(dungeons))]

    def dfs(k):
        best = 0
        for i in range(len(dungeons)):
            if visited[i] or k < dungeons[i][0]:
                continue
            visited[i] = True
            best = max(best, 1 + dfs(k - dungeons[i][1]))
            visited[i] = False
        return best
    return dfs(k)
