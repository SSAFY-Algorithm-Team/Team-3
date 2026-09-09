# from collections import deque

# def solution(scoville, K):
    
#     answer = 0
#     while min(scoville) < K:
#         scoville = list(scoville)
#         scoville.sort()
#         scoville = deque(scoville)
#         a = scoville.popleft()
#         b = scoville.popleft()
#         scoville.append(a + b * 2)
#         answer += 1
#     return answer

# 프로그래머스 Lv2. 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 소요시간: 10분 / 시도: 2회

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)          # O(n), 리스트를 힙으로
    answer = 0

    while scoville[0] < K:           # 힙의 0번은 항상 최솟값
        if len(scoville) < 2:        # 섞을 짝이 없으면 불가능
            return -1
        a = heapq.heappop(scoville) # O(logn)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b * 2) # O(logn)
        answer += 1

    return answer