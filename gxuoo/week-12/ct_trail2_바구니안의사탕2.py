# 코드트리 Trail2. 바구니 안의 사탕 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-candy-in-the-basket-2/description

N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
MAX_POS = 100
arr = [0] * (MAX_POS + 1)
for c, p in zip(candy, pos):
    arr[p] += c

ans = 0
for center in range(MAX_POS + 1):
    left = max(0, center - K)
    right = min(MAX_POS, center + K)
    ans = max(ans, sum(arr[left:right + 1]))

print(ans)
