# 코드트리 Trail2. 원 모양으로 되어있는 방
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-a-room-in-a-circle/description

n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
ans = float('inf')
for s in range(n):
    total = 0
    for j in range(n):
        total += a[(s + j) % n] * j
    ans = min(ans, total)

print(ans)
