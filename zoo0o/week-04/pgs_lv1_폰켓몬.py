# 프로그래머스 Lv1. 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 소요시간: 3분 / 시도: 1회

def solution(nums):
    # 1. 중복을 제거해 폰켓몬 종류 수 확인
    cards = set(nums)

    # 2. 고를 수 있는 수(N/2)보다 종류가 많으면 N/2개 선택
    if len(cards) > len(nums) // 2:
        return len(nums) // 2

    # 3. 종류가 더 적으면 존재하는 종류 수만큼 선택
    else:
        return len(cards)

    # return min(len(set(nums)), len(nums) // 2)