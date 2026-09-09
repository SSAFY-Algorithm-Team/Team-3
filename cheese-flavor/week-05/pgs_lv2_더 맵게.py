# 프로그래머스 Lv2. 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 소요시간: 15분 / 시도: 2회

import heapq

def solution(scoville, K):
    heapq.heapify(scoville) #힙으로 바꿔
    count = 0
    
    #min(scoville) -> scoville[0] // 복잡도 낮춤!
    while scoville[0] < K:
        if len(scoville) >= 2: #길이가 2 이상일때만 / 1개만 남으면 계산 안되니까
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + second*2)
            count += 1
        # 2개 미만일경우 바로 리턴
        else:
            return -1
        
    return count

    
            
            
            
        
    


