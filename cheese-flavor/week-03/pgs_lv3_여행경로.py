# 프로그래머스 Lv3. 여행경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 소요시간: 80분 / 시도: 4회


def solution(tickets):
    
    '''
    - dfs로 경로 다 찾고 -> 경로명이 겹치는 곳은 어떻게 처리?  인덱스 번호로?
    - for 문으로 같지 않는곳을 비교한 다음
      - 기준: 2 경로씩 비교하는게 빠를까?
             초기경로를 하나 집어놓은 상태에서?
    '''
    
    #변수 정의
    answer, n = [], len(tickets)
    path = ['ICN']
    visited = [False] * n
    
    def dfs(start):    # start == ICN인지 판명하는 부분이 밖에서 진행되야하나?
        nonlocal path
        if len(path) == n+1:
            answer.append(path[:]) #초기화할께 아니라면 복사본으로 진행
        
        
        for i in range(n):
            if tickets[i][0] == start and not visited[i]:
                visited[i] = True
                path.append(tickets[i][1])
                
                dfs(tickets[i][1])
                visited[i] = False
                path.pop() #차피 마지막꺼 밸꺼고 인덱스값으로만 인식가능
                
    dfs("ICN")
    
    best = answer[0]
    
    # 다경로일 경우 해결책
    for i in range(1, len(answer)):
        if best > answer[i]:
            best = answer[i]
    
    return best
    
    
''' -> 리스트 비교만으로도 사전순으로 대체 가능
    # 다경로일 경우 해결책    
    root_len = len(''.join(best))
    
    if len(answer) == 1:
        return best
    
    else:
        for i in range(1, len(answer)):
            for j in range(3, root_len):
                if ''.join(best)[j] != ''.join(answer[i])[j]:
                    if ord(''.join(best)[j]) > ord(''.join(answer[i])[j]):
                        best = answer[i]
        
        return best

'''
