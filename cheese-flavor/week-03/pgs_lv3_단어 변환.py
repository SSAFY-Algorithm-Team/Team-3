# 프로그래머스 Lv3. 단어 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 소요시간: 80분 / 시도: 3회


from collections import deque

def solution(begin, target, words):
    
    '''
    - begin은 words안에 없어도 되고, target은 words안에 있어야하네 -> 이거땜에 별짓을 다함 ;;
    - 1. 끝단어 여부를 파악해서 return 0으로 시작
    - 2. bfs로 풀기 ->  한글자만 차이나도록 letter_count가 1인지 -> bfs 로직 까먹어서 다시 공부
    - 3. 최소지점은 현재 글자가 한글자만 차이나는지 = return count (최소 스텝)
    '''
    visited = [False] * len(words)
    
        
    if target not in words:
        return 0
    else:
        q = deque()
        q.append((begin,target,1)) #return 할땐 target과 비교 / for문 순환할땐 begin과 비교
        
        while q:
            begin, target, count = q.popleft()
            
            #return 정의
            letter_count = 0
            for i in range(len(target)):    #여기부분을 더 간소화 할 수 있는 방법이 있나?       
                if begin[i] != target[i]:
                    letter_count += 1
            if letter_count == 1:
                return count
            
            #bfs 구조 짜기
            for j in range(len(words)):
                letter_count = 0
                for i in range(len(begin)):
                    if begin[i] != words[j][i]:
                        letter_count += 1
                
                if letter_count == 1 and not visited[j]:
                    visited[j] = True
                    q.append((words[j], target, count+1))

                    
                    
