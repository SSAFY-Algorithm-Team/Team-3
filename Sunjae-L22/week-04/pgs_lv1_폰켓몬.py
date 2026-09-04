# 프로그래머스 Lv1. 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 소요시간: 5분 / 시도: 1회

from collections import Counter

def solution(nums):
    answer = 0
    poketmon_count = Counter(nums)
    N = len(nums)

    if len(poketmon_count) >= N//2:
        answer = N//2
    else:
        answer = len(poketmon_count)

    return answer

nums = [3, 3, 3, 2, 2, 4]
print(solution(nums))