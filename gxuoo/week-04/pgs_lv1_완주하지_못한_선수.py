# 프로그래머스 Lv1. 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 소요시간: 20분 / 시도: 2회

from collections import Counter

def solution(participant, completion):
    diff = Counter(participant) - Counter(completion)
    return list(diff)[0]
