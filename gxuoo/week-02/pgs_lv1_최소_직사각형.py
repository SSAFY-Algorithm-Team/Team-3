# 프로그래머스 Lv1. 최소 직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 소요시간: 20분 / 시도: 2회

def solution(sizes):
    for idx in range(len(sizes)):
        if sizes[idx][0] < sizes[idx][1]:
            sizes[idx][0], sizes[idx][1] = sizes[idx][1], sizes[idx][0]

    max_width = max([sizes[i][0] for i in range(len(sizes))])
    max_height = max([sizes[i][1] for i in range(len(sizes))])
    return max_width * max_height
