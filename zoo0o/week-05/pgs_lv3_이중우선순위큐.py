# 프로그래머스 Lv3. 이중우선순위큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# AI

import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    deleted = [False] * len(operations)

    for idx, operation in enumerate(operations):
        command, number = operation.split()
        number = int(number)

        # 1. 숫자 삽입
        if command == "I":
            heapq.heappush(min_heap, (number, idx))
            heapq.heappush(max_heap, (-number, idx))

        # 2. 최솟값 삭제
        elif command == "D" and number == -1:
            # 이미 다른 힙에서 삭제된 값 제거
            while min_heap and deleted[min_heap[0][1]]:
                heapq.heappop(min_heap)

            if min_heap:
                _, delete_idx = heapq.heappop(min_heap)
                deleted[delete_idx] = True

        # 3. 최댓값 삭제
        elif command == "D" and number == 1:
            # 이미 다른 힙에서 삭제된 값 제거
            while max_heap and deleted[max_heap[0][1]]:
                heapq.heappop(max_heap)

            if max_heap:
                _, delete_idx = heapq.heappop(max_heap)
                deleted[delete_idx] = True

    # 4. 마지막에 남아있는 삭제된 값 정리
    while min_heap and deleted[min_heap[0][1]]:
        heapq.heappop(min_heap)

    while max_heap and deleted[max_heap[0][1]]:
        heapq.heappop(max_heap)

    # 5. 큐가 비어있는 경우
    if not min_heap:
        return [0, 0]

    max_value = -max_heap[0][0]
    min_value = min_heap[0][0]

    return [max_value, min_value]