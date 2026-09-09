# 프로그래머스 Lv1. 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

from collections import deque

def solution(arr):
    answer = []
    ans_queue = deque([arr[0]])

    for i in range(1,len(arr)):
        if arr[i-1] == arr[i]:
            continue
        else:
            ans_queue.append(arr[i])

    for _ in range(len(ans_queue)):
        answer.append(ans_queue.popleft())
    print(answer)
    return answer

solution([1,1,3,3,0,1,1])