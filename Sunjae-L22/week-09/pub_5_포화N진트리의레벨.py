# 포화N진트리의레벻
# 소요시간 : 

# 음..연결 개수가 1이면 리프 노드...
# 연결 개수가 2 이상인 것 중에 가장 작은게 리프 노드
from collections import deque

v = 7
edges = [[3,4], [4,0], [2,1], [6,1], [1,3], [4,5]]

def solution(v, edges):
    # 1개면 레벨 [1] 반환
    if v == 1:
        return [1]

    # 무방향 그래프
    graph = [[] for _ in range(v)]

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # 리프를 제외하고, 연결 개수가 가장 적은 노드 찾기
    root = -1
    min_count = v + 1

    for node in range(v):
        count = len(graph[node])

        if count >= 2 and count < min_count:
            root = node
            min_count = count

    # 루트부터 BFS로 레벨 계산
    level = [0] * v
    level[root] = 1
    queue = deque([root])

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            # 아직 방문 안했으면 -> level이 0이면으로 판단
            if level[next_node] == 0:
                level[next_node] = level[node] + 1
                queue.append(next_node)

    return level