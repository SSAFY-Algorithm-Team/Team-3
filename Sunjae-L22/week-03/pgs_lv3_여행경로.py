# 프로그래머스 Lv3. 여행경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 소요시간: 50분 / 시도: 2회

from collections import defaultdict, deque

def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    # 사전순을 보장하기 위해 첨부터 정렬
    for k in graph:
        graph[k].sort()

    # 티켓 사용했는지 여부
    used = {k : [False] * len(v) for k, v in graph.items()}
    m = len(tickets)
    path = ["ICN"]

    def dfs(now):
        # 티켓을 다 썼을 경우 완성됨
        if len(path) == m + 1:
            return True
        for i, next in enumerate(graph[now]):
            if used[now][i]:
                continue
            used[now][i] = True
            path.append(next)
            # if문 안해주면 뒤에 pop이 실행되어버림
            if dfs(next):
                return True
            path.pop()
            used[now][i] = False
        return False

    dfs("ICN")
    return path