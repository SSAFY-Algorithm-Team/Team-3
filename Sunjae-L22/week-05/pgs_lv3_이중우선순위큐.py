# 프로그래머스 Lv3. 이중우선순위큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# 소요시간: 50분 / 시도: 1회

import heapq

def solution(operations):
    h = []
    for op in operations:
        cmd, n = op.split()
        if cmd == "I":
            heapq.heappush(h, int(n))
        elif h:                    # 비어있으면 무시
            if n == "1":
                h.remove(max(h))   # 최댓값 찾아서 빼기
                heapq.heapify(h)   # 다시 힙으로
            else:
                heapq.heappop(h)   # 최솟값은 그냥 pop
    return [max(h), min(h)] if h else [0, 0]