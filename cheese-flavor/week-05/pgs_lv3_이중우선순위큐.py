# 프로그래머스 Lv3. 이중우선순위큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# 소요시간: 150분 / 시도: 7회


#구조적으로 어떻게 구성하지를 먼저 생각해야할듯?
#시간을 너무 많이 써먹고 흐름이 잘 안잡힘 ;;

import heapq
def solution(operations):
    
    # 최소값 기준, 최대값 기준 리스트로 진행?
    min_heap = []
    max_heap = []
    
    id = 0  #고유값 기반으로 리스트 두개 중에 삭제할 값을 선택해두려고
    deleted = set() #삭제할 인덱스값 저장용
    live_count = 0 #실제값 개수 확인용
    
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    
    
    # 실제 존재값인지 확인하는 함수
    def check_real(heap):
        nonlocal live_count
        heap_len = len(heap)
        
        while heap and heap[0][1] in deleted:
            heapq.heappop(heap)  # 존재하지않으면 제거
            live_count -= 1 #실제값을 -1
        
    
    for oper in operations:
        o, n = oper.split() # 분리해서 저장
        n = int(n)
        
        check_real(min_heap)
        check_real(max_heap)
        
        if o == 'I':  # |이 아니라 I네.. ;;
            heapq.heappush(min_heap, (n, id))
            heapq.heappush(max_heap, (-n, id))
            live_count += 1
            id += 1
        
        #여기선 실제로 양옆 리스트에서 제거한게 아니니까 REAL값 줄이기 X
        elif o == 'D':
            if min_heap and n == -1:
                deleted.add((heapq.heappop(min_heap))[1])
                
            elif max_heap and n == 1:
                deleted.add((heapq.heappop(max_heap))[1])
                
        # POP 진행후에 리얼값 재점검
        check_real(min_heap)
        check_real(max_heap)
                    
    if live_count == 0:
        return [0,0]
    
    else:
        return [-(max_heap[0][0]), min_heap[0][0]]


    
            
            
            
        
    


