# 프로그래머스 Lv2. 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 소요시간: 20분 / 시도: 2회

def solution(priorities, location):
    answer = 0
    index = 0

    while priorities:
        # 현재 위치부터 원형으로 돌며 최고 우선순위 찾기
        while priorities[index] != max(priorities):
            index = (index + 1) % len(priorities)

        answer += 1
        del priorities[index]

        # 목표였다면 종료, 아니면 location 보정
        if index == location:
            return answer
        if index < location:
            location -= 1

        if priorities:
            index %= len(priorities)

    return answer
