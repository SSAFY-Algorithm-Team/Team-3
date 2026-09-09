# 프로그래머스 Lv2. 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 소요시간: 15분 / 시도: 1회

from collections import deque

def solution(progresses, speeds):
    queue = deque()
    for i in range(len(progresses)):
        queue.append([progresses[i], speeds[i]])

    answer = []
    while queue:
        for task in queue:
            task[0] += task[1]

        count = 0
        while queue and queue[0][0] >= 100:
            queue.popleft()
            count += 1

        if count > 0:
            answer.append(count)

    return answer
