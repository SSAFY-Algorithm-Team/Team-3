# 코드트리 Trail2. 가장 가까운 두 점 사이의 거리
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-closest-pair-of-points/description

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
ans = float('inf')
for i in range(n):
    for j in range(i + 1, n):
        dist = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
        ans = min(ans, dist)

print(ans)
