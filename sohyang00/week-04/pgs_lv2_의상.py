# 프로그래머스 Lv2. 의상
# https://school.programmers.co.kr/learn/courses/30/lessons/42578


def solution(clothes):
    look = {}
    combinations = 1
    for _, key in clothes:
        look[key] = look.get(key, 0) + 1

    for count in look.values():
        combinations *= count + 1

    return combinations -1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])