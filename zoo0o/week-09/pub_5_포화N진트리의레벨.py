def solution(v, edges):
    # degree 1 → leaf
    # degree 2 → root
    # degree 3 → 중간 노드
    
    maps = [[0]*v for _ in range(v)] 
    
    degree = [0] * v       # 노드별 연결 개수
    visited = [False] * v  # DFS 방문 여부
    levels = [0] * v
    
    root = -1 
    

    def dfs(start, level):
        visited[start] = True
        levels[start] = level

        # start보다 작은 번호
        for i in range(0, start):
            if maps[i][start] == 1 and not visited[i]:
                dfs(i, level + 1)

        # start보다 큰 번호
        for i in range(start + 1, v):
            if maps[start][i] == 1 and not visited[i]:
                dfs(i, level + 1)
     # edge를 2차원 격자로
    for a, b in edges:
        # 무조건 a가 더 작도록
        if a > b:
            a, b = b, a

        maps[a][b] = 1

        degree[a] += 1
        degree[b] += 1

    # N 찾기
    # leaf는 degree=1
    # root는 degree=N
    # 중간 노드는 degree=N+1
    N = min(x for x in degree if x > 1)

    # degree가 N인 노드가 root
    for i in range(v):
        if degree[i] == N:
            root = i
            break

    dfs(root, 1)

    return levels