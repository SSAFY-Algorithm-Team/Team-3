def solution(nums):
    dogam = {}
    for n in nums:
        if n not in dogam:
            dogam[n] = 1
        else:
            dogam[n] += 1
    answer = min(len(nums)//2, len(dogam))
    return answer