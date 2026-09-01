# 프로그래머스 Lv1. 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 구현 > AI 사용 : 사유 딕셔너리 모름...

def solution(nums):
    cards = set(nums)
    if len(cards) > len(nums)//2:
        return len(nums)//2
    else:
        return len(cards)

    # return min(len(set(nums)), len(nums) // 2)