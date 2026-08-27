def solution(tickets):
    answer = []
    # visited 배열 생성
    visited = [0 for _ in range(len(tickets))]
    
    def dfs(current_flight, route):
        nonlocal answer
        # 항공권 다 돌았는가
        if visited.count(1) == len(tickets):
            answer.append(route[:])
            return
        
        for idx, ticket in enumerate(tickets):
            # 방문한 적 없는 항공권이면서 티켓 맨 앞이 현재 위치라면
            if visited[idx] == 0 and ticket[0] == current_flight:
                # 방문 처리 및 경로에 추가
                visited[idx] = 1
                route.append(ticket[1])
                dfs(ticket[1], route)
                # 백트래킹
                visited[idx] = 0
                route.pop()
        
    dfs("ICN", ["ICN"])
    final = answer[0]
    
    # 경로 알파벳 순으로 비교
    if len(answer) >= 2:
        for ans in answer:
            # 알파벳으로 비교가 완료되었는지
            flag = False
            # 각각 요소마다 비교
            for final_char, ans_char in zip(final, ans):
                # 요소가 다르면!
                if final_char != ans_char and not flag:
                        # 알파벳마다 비교
                        if final_char > ans_char:
                            # 더 앞선 순서의 알파벳을 final에 저장
                            final = ans
                            flag = True
                        break
    print(final)
    return final