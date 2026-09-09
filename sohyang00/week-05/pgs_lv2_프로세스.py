# 프로그래머스 Lv2. 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))
    count = 0

    while queue:
        max_priority = max(p for _, p in queue)
        idx, priority = queue.popleft()

        if priority < max_priority:
            queue.append((idx, priority))
        else:
            count += 1
            if idx == location:
                return count