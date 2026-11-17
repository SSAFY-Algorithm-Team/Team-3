import sys
sys.stdin = open("sample_input.txt","r")

from collections import deque

def bfs(vertex):
    q = deque([vertex])

    while q:
        v = q.popleft()
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    return 1

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [False]*(N+1)

for start in range(1,N+1):
    if not visited[start]:
        visited[start] = True
        count += bfs(start)

print(count)

