# 프로그래머스 Lv2. 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586
import math

def solution(progresses, speeds):
    answer = []
    release_day = 0
    count = 0

    for progress, speed in zip(progresses, speeds):
        days_needed = math.ceil((100 - progress) / speed)

        # 현재 작업일이 이전보다 길고
        if days_needed > release_day:
            if count: #기존 카운트가 있다면 (처음 작업 append 방지)
                answer.append(count)

            release_day = days_needed
            count = 1
        else:
            count += 1

    #남은 카운트가 있다면
    if count:
        answer.append(count)

    return answer
