# 프로그래머스 Lv2. 의상
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    # 1. 의상 종류별 개수 저장
    clothes_dict = {}

    for name, category in clothes:
        if category not in clothes_dict:
            clothes_dict[category] = 0
        clothes_dict[category] += 1

    answer = 1

    # 2. 각 종류의 (옷 개수 + 안 입는 경우)를 모두 곱함
    for category in clothes_dict:
        answer *= clothes_dict[category] + 1

    # 3. 아무것도 입지 않는 경우 제외
    return answer - 1