# 프로그래머스 Lv1. 최소직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 소요시간: 5m / 시도: 1회

# [[60, 50], [30, 70], [60, 30], [80, 40]]	4000
# [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	120
# [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	133

# 가로가 항상 길게 바꿔두고 최댓값 구하기

def solution(sizes):
    answer = 0
    # TODO: 모든 명함을 수납할 수 있는 가장 작은 지갑의 크기를 구한다.

    max_w, max_h = 0,0

    for width, height in sizes:
        if width < height:
            width, height = height, width
        max_w = max(width, max_w)
        max_h = max(height, max_h)

    answer = max_w*max_h

    return answer
