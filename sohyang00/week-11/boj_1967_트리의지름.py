import sys
sys.stdin = open("sample_input.txt", "r")

from collections import deque

def bfs(start):
    graph[start].sord(reverse = True, key=lambda x:x[1])
    dist= [[-1] for _ in range(len(graph))]
    dist[start] = 0 
    q = deque(graph[start])

    while q:
        next_node, cost = q.popleft()
        if dist[next_node] == -1:
            dist[next_node] += cost

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    pn, cn, cost = map(int, input().split())
    graph[pn].append((cn, cost))
    graph[cn].append((pn, cost))
# graph[4].sort(reverse=True, key=lambda x:x[1])
# 노드 자식 코스트 높은 순으로 정렬해서 최장거리 구하기
# sort(lamda x:x[1]) 이렇게였던가 땡
# sort(reverse = True, key = lambda x:x[1]) 이거임

# 모든 노드에서 다 시작하기
for i in range(len(graph)):
    bfs(i)
