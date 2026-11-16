# 코드트리 Trail2. 구간 중 최대 합
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-max-sum-of-subarray/description

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
res = 0
for i in range(n - k + 1):
    arr2 = arr[i:i+k]
    res = max(res, sum(arr2))

print(res)
