# 기출 5. 포화 N진 트리의 레벨
# 소요시간: 40분 / 시도: 3회

from collections import deque


def solution(v, edges):
    graph = [[] for _ in range(v)]

    # 간선 정보 수집
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # 노드가 하나
    if v == 1:
        return [1]

    # 자식을 가진 노드(차수 > 1)만 모으기
    internal = []
    for i in range(v):
        if len(graph[i]) > 1:
            internal.append(i)

    # 루트 찾기
    if len(internal) == 1:
        # 루트 + 리프만 있는 경우
        root = internal[0]
    else:
        max_degree = 0
        for i in internal:
            max_degree = max(max_degree, len(graph[i]))
        for i in internal:
            # 루트 차수 = N = (N+1) - 1
            if len(graph[i]) == max_degree - 1:
                root = i
                break

    # BFS 로 레벨 계산
    level = [0] * v
    level[root] = 1
    q = deque([root])

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if level[nxt] == 0:
                level[nxt] = level[cur] + 1
                q.append(nxt)

    return level


if __name__ == "__main__":
    print(solution(7, [[3, 4], [4, 0], [2, 1], [6, 1], [1, 3], [4, 5]]))  # [3, 2, 3, 1, 2, 3, 3]
    print(solution(5, [[1, 0], [1, 2], [3, 1], [4, 1]]))  # [2, 1, 2, 2, 2]
