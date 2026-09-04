# 프로그래머스 Lv1. 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 소요시간: 10분 / 시도: 1회


def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1]
