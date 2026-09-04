# 프로그래머스 Lv1. 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    counts = {}
    for name in participant:
        counts[name] = counts.get(name,0) + 1

    for name in completion:
        counts[name] -= 1

    for name, count in counts.items():
        if count > 0:
            return name
