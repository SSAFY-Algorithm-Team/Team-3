# 프로그래머스 Lv1. 최소 직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 소요시간: 8분 / 시도: 1회

def solution(sizes):
    long, short = 0, 0  # 긴 애들 한쪽으로 모으기
    
    for wallet in sizes:
        if wallet[0] >= wallet[1]:
            long = max(long, wallet[0])
            short = max(short, wallet[1])
        
        else:
            long = max(long, wallet[1])
            short = max(short, wallet[0])

    return long * short
