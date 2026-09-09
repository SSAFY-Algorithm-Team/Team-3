# 프로그래머스 Lv2. 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 소요시간: 3분 / 시도: 1회

def solution(s):
    answer = True
    open = []
    for _ in s:
        if _ == '(':
            open.append(_)
        else:
            if len(open) == 0:
                answer = False
            else:
                open.pop()
    if len(open) > 0:
        answer = False

    return answer