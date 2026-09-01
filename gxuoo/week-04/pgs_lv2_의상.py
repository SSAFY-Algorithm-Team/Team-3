# 프로그래머스 Lv2. 의상
# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 소요시간: 30분 / 시도: 2회

def solution(clothes):
    count = {}
    for name, kind in clothes:
        count[kind] = count.get(kind, 0) + 1
        
    answer = 1
    for n in count.values():
        answer *= (n + 1)
    return answer - 1
