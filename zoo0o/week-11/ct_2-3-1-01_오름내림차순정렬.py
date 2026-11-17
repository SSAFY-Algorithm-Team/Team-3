# 코드트리 2-3-1-01. 오름내림차순정렬
# *nums: 리스트를 풀어서 원소를 하나씩 전달
# 예: nums = [3, 5, 6]일 때 print(*nums) → 3 5 6

n = int(input())
nums = list(map(int, input().split()))

# 오름차순: 작은 수부터
nums.sort()
print(*nums)

# 내림차순: 큰 수부터
nums.sort(reverse=True)
print(*nums)
