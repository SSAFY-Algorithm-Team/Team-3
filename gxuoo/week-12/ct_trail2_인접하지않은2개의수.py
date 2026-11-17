# 코드트리 Trail2. 인접하지 않은 2개의 수
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-two-non-adjacent-numbers/description

n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
res = 0
for i in range(n):
    for j in range(n):
        if abs(i - j) <= 1:
            continue
        
        res = max(res, numbers[i] + numbers[j])

print(res)
