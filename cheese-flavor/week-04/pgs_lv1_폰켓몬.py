# 프로그래머스 Lv1. 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 소요시간: 10분 / 시도: 1회


def solution(nums):
    kind = len(set(nums)) #겹치지 않고 가능한 횟수
    pick = len(nums)//2  #최소 절반값
    
    return min(kind, pick)
    
'''
def solution(nums):
    nums2 = []
        
    for i in range(len(nums)):
        if nums[i] not in nums2:
            nums2.append(nums[i])
            
    if len(nums2) >= (len(nums)//2):
        return len(nums)//2
    else:
        return len(nums2)
'''