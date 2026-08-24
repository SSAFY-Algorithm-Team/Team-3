# 프로그래머스 Lv3. 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 소요시간: 40분 / 시도: 2회


def solution(n, computers):
    '''
    - visited로 방문은 할껀데, 계속 연결되어 있으면 하나라고 생각
    - 계속 연결되어있음을 나타내기위해 체크하는 리스트가 하나 필요할꺼 같기도?
      -> 리스트나 count하나 똑같으니까 그냥 정수로 출력하자 len 형태말구
    '''
    
    count = 0
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        for j in range(n):
            if computers[node][j] == 1 and not visited[j]:
                dfs(j)
                
                
    for i in range(n):
        if not visited[i]:
            count += 1  #카운트는 네트워크당 1번
            dfs(i)
            
    return count
