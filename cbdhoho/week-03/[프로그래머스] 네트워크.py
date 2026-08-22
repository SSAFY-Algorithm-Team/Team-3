# 이것또한 ai의 도움을... 받았습니다.처음에는 문제 이해를 잘 못해서 헤맸습니다. 방문하지 않은 노드라면 dfs를 돌렸습니다.

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def dfs(node):
        visited[node] = True
        
        for i in range(n):
            if computers[node][i] == 1 and visited[i] == False:
                dfs(i)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer