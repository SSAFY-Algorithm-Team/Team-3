# 프로그래머스 Lv3. 디스크 컨트롤러
# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 소요시간: 70분 / 시도: 4회


import heapq
def solution(jobs):
    
    current_time = 0 #프로세스 시각
    heap = []  #하드디스크
    finished = 0 #while문에 쓰려고
    total_time = 0 #최종 합산값
    n = len(jobs)
    jobs.sort() # 혹시나해서 진행
    
    '''
    1. 프로세스 시간이 진행되는동안, 해당 시간보다 같거나 작은것을 다 큐에 넣음
    2. 우선순위 큐로 저장할때 (작업진행시간, 요청시간) -> 우선순위를 작업진행으로
       -> 굳이 인덱스값이 필요없었으
    3. 큐가 있으면 우선순위 따라 빼면서 계산식 진행
    '''
    
    while finished < n:
        
        #요청시간보다 같거나 작은 애들 큐에 다 넣기
        while jobs and jobs[0][0] <= current_time:
            heapq.heappush(heap, (jobs[0][1], jobs[0][0]))
            jobs.pop(0)
        
        #비어있으면 1씩 증가가 아니라 다음 작업으로 가게끔
        if not heap:
            current_time = jobs[0][0] 
            
        else:
            process, arrive = heapq.heappop(heap)
            current_time += process
            finished += 1
            total_time += (current_time-arrive)    
        
    return int(total_time/n)


    
            
            
            
        
    


