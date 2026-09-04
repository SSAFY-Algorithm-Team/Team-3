# 프로그래머스 Lv1. 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 구현 > AI 사용 : 사유 딕셔너리 모름...

def solution(participant, completion):
    # 1. 참가자별 인원 수 저장
    player = {}

    for name in participant:
        if name in player:
            player[name] += 1
        else:
            player[name] = 1

    # 2. 완주한 선수의 인원 수 감소
    for name in completion:
        player[name] -= 1

    # 3. 1명이 남아 있는 선수가 미완주자
    for name in player:
        if player[name] == 1:
            return name