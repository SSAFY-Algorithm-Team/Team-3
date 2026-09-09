# 프로그래머스 Lv2. 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 소요시간: 25분 / 시도: 5회

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        min1 = heapq.heappop(scoville)
        if min1 < K:
            if not len(scoville):
                return -1
            min2 = heapq.heappop(scoville)
            new_value = min1 + min2 * 2
            heapq.heappush(scoville, new_value)
            answer += 1
        else:
            heapq.heappush(scoville, min1)
            break

    return answer
