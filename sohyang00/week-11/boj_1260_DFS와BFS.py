from collections import deque

import sys
sys.stdin = open("sample_input.txt", "r")

def dfs(v):
    global dfs_result
    dfs_visited[v] = True
    dfs_result.append(v)
    for vertex in graph[v]:
        if not dfs_visited[vertex]:
            dfs(vertex)
        else:
            continue

def bfs(v):
    global bfs_result
    q = deque([v])
    bfs_visited[v] = True

    while q:
        curr = q.popleft()
        bfs_result.append(curr)

        for vertex in graph[curr]:
            if not bfs_visited[vertex]:
                bfs_visited[vertex] = True
                q.append(vertex)

n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
dfs_result = []
bfs_result = []

dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

for arr in graph:
    arr.sort()

dfs(v)
bfs(v)
print(dfs_result)
print(bfs_result)