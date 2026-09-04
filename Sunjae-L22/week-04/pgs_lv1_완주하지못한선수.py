# 프로그래머스 Lv1. 완주하지못한선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 소요시간: 5분 / 시도: 1회

from collections import Counter

def solution(participant, completion):
    diff = Counter(participant) - Counter(completion)
    failer = list(diff.elements())
    return failer[0]