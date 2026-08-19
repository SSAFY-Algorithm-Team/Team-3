# 프로그래머스 Lv2. 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 소요시간: 50분 / 시도: 2회

#경로 자체를 하나의 리스트로 만들어서 진행하는 형태로 제작

def solution(k, dungeons):
    answer, n, path = 0, len(dungeons) , []   
    visited = [False] * n
    
    #구조가 조금 더 익으면 괜찮을듯?
    def dfs(semi_path):
        
        for i in range(n):  #순서를 도는 것
            if len(semi_path) == n:
                path.append(semi_path)
            
            if not visited[i]:
                visited[i] = True
                
                #집어넣을때 새로만드니까 초기화 필요 x / 공유 x
                dfs(semi_path + [dungeons[i]]) 
                
                visited[i] = False
    
    dfs([])
    #return path  #확인용

    # 피로도 로직
    for root in path:
        new_k, semi_answer = k, 0 
        
        for dungeon in root:
            if new_k >= dungeon[0]:
                new_k -= dungeon[1]
                semi_answer += 1
                
            else:
                break
        
        answer = max(answer, semi_answer)

    return answer
    