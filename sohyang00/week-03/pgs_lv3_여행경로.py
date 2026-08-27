# 프로그래머스 Lv3. 여행경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164

# 모든 거리 중에서 알파벳이 앞선 순서 
# 끝까지 가야하니까 DFS 
# 경로, 임시경로 두 가지 만들어서 하나 씩 비교.
# 같으면 continue, 다르면 알파벳 낮은 걸 현재 경로로 바꾸고 break

def solution(tickets):
    n = len(tickets)
    visited = [False] * n #티켓 처리
    route = ["ICN"]

    tickets.sort(key=lambda 
                 ticket: ticket[1])
    
    def dfs(curr, route): #현재 공항, 공항 경로
        if len(route) == n+1:
            return True
        
        for i in range(n):
            departure, arrival = tickets[i]

            if departure == curr and not visited[i]:
                visited[i] = True
                route.append(arrival)
                if dfs(arrival, route):
                    return True
                route.pop()
                visited[i] = False
        return False

        # 알파벳 비교

    dfs("ICN", route)
    print(route)
    return route

solution([["ICN", "SFO"], ["ICN", "ATL"], 
          ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])