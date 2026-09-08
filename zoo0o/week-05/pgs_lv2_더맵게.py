# 프로그래머스 Lv2. 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# AI > 힙 사용법 찾아봄

import heapq

def solution(scoville, K):
    # 힙으로 만들기
    heapq.heapify(scoville)
    answer = 0

    # scoville[0]: 항상 가장 작은 값
    while scoville[0] < K:

        # 2개를 섞어야 하는데 음식이 1개만 남으면 불가능
        if len(scoville) < 2:
            return -1

        # 가장 작은 값 2개 꺼내기
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        mixed = first + second * 2

        # 섞은 음식 다시 넣기
        heapq.heappush(scoville, mixed)

        answer += 1

    return answer