# 프로그래머스 Lv2. 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 소요시간: 10분 / 시도: 1회

from collections import deque

def solution(priorities, location):
    q = deque(enumerate(priorities))   # (원래 위치, 우선순위)
    count = 0
    while q:
        cur = q.popleft()
        if any(cur[1] < p for _, p in q):
            q.append(cur)              # 더 높은 놈 있으면 뒤로
        else:
            count += 1                 # 실행
            if cur[0] == location:
                return count