# 프로그래머스 Lv2. 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909
from collections import deque
def solution(s):
    answer = True
    stack = [] 
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            if stack.pop() == '(':
                continue
    if stack:
        return False
    return True

solution("(())()")