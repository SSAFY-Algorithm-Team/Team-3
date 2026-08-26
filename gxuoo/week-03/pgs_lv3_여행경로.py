# 프로그래머스 Lv3. 여행경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 소요시간: 50분 / 시도: 1회

def solution(tickets):
    tickets.sort()
    visited = [False] * len(tickets)
    answer = []
    
    def dfs(cur_airport, path):
        if len(path) == len(tickets) + 1:
            answer.extend(path)
            return True
        
        for idx in range(len(tickets)):
            departure, arrival = tickets[idx]
            if not visited[idx] and cur_airport == departure:
                visited[idx] = True
                if dfs(arrival, path + [arrival]):
                    return True
                visited[idx] = False    
        
        return False
        
    dfs("ICN", ["ICN"])
    return answer
