# 프로그래머스 Lv1. 같은숫자는싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 소요시간: 3분 / 시도: 1회

def solution(arr):
    answer = [arr[0]]
    last = arr[0]
    for num in arr:
        if num == last:
            continue
        last = num
        answer.append(num)
    return answer