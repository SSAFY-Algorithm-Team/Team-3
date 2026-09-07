# 프로그래머스 Lv2. 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 구현 AI

from collections import deque

def solution(priorities, location):
    # (원래 위치, 우선순위)를 큐에 저장
    queue = deque()

    for i in range(len(priorities)):
        queue.append((i, priorities[i]))

    count = 0

    while queue:
        idx, priority = queue.popleft()

        # 현재보다 우선순위가 높은 프로세스가 남아 있으면 뒤로 이동
        if any(priority < q_priority for _, q_priority in queue):
            queue.append((idx, priority))

        # 높은 프로세스가 없으면 실행
        else:
            count += 1

            # 찾던 프로세스가 실행되면 실행 순서 반환
            if idx == location:
                return count