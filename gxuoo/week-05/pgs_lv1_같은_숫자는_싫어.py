# 프로그래머스 Lv1. 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 소요시간: 5분 / 시도: 1회

def solution(arr):
    answer = []
    for value in arr:
        if not len(answer):
            answer.append(value)

        if value != answer[len(answer) - 1]:
            answer.append(value)
    return answer
