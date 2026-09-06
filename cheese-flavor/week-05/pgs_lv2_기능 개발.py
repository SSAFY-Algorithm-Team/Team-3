# 프로그래머스 Lv2. 기능 개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3
# 소요시간: 40분 / 시도: 2회


def solution(progresses, speeds):

    ''' 그냥 재귀로 할껄 ;;
    1. 각 작업당 걸리는 일자를 day 리스트 생성
    2. 각 작업 방문했는지 여부 리스트 생성
    3. 작업날짜가 증가할때마다 day가 이보다 작으면 카운트 / 이후 작업도(for문)
    4. 최종 count를 answer에 추가
    '''
    
    day, answer = [], []
    n = len(progresses)
    visited = [False] * n
    
    # day 리스트 생성
    for i in range(n):
        count = 0
        
        #이렇게 계산이 더 나을듯
        if (100 - progresses[i]) % speeds[i] == 0:
            day.append((100 - progresses[i]) // speeds[i])
        
        else:
            day.append((100 - progresses[i]) // speeds[i]+1)
            
        ''' 시간 많이 잡아먹을까봐 위와 같이 수정함
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            count += 1

        day.append(count)  
        '''

    # 배포 몇개 가능한지
    for i in range(day[0], max(day)+1):
        day_count = 0
        
        for j in range(n):
            if not visited[j]:
                if day[j] <= i:
                    visited[j] = True
                    day_count += 1
                    
                else:
                    break #한번이라도 이전작업의 크기보다 크면 바로 종료
                
        if day_count != 0:
            answer.append(day_count)
    
    return answer

            
            
            
        
    


