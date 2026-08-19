def solution(k, dungeons):
    answer = -1
    visited = [False] * len(dungeons)
    
    def dfs(current_p, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        
        for i in range(len(dungeons)):
            if not visited[i] and current_p >= dungeons[i][0]:
                visited[i] = True
                dfs(current_p - dungeons[i][1], cnt + 1)
                visited[i] = False
    dfs(k, 0)
    return answer