# 프로그래머스 Lv2. 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 소요시간: 10분 / 시도: 1회

def solution(s):
    arr = []
    for value in s:
        if value == '(':
            arr.append(value)
        else:
            if not len(arr):
                return False
            arr.pop()
            
    if len(arr):
        return False

    return True
