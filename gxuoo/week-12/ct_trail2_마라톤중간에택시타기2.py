# 코드트리 Trail2. 마라톤 중간에 택시타기 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-taking-a-taxi-in-the-middle-of-the-marathon-2/description

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
def dist(a, b):
    return abs(x[a] - x[b]) + abs(y[a] - y[b])

origin_total = 0
for i in range(n - 1):
    origin_total += dist(i, i + 1)

ans = float('inf')
for i in range(1, n - 1):
    total = origin_total - dist(i - 1, i) - dist(i, i + 1) + dist(i - 1, i + 1)
    ans = min(ans, total)

print(ans)
