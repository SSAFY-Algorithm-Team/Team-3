# 프로그래머스 Lv1. 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 소요시간: 30분 / 시도: 1회

def solution(nums):
    return min(len(set(nums)), len(nums) // 2)
