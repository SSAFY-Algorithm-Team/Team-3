# 코드트리 Trail2. 좌표평면 위의 특정 구역 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-specific-zone-above-the-2d-coordinate-2/description

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
ans = float('inf')
for i in range(n):
    # i번째 인덱스 제외하고 나머지 n-1개의 점을 가지고 직사각형 계산
    min_x, max_x = float('inf'), float('-inf')
    min_y, max_y = float('inf'), float('-inf')
    for j in range(n):
        if j == i:
            continue
        min_x = min(min_x, x[j])
        max_x = max(max_x, x[j])
        min_y = min(min_y, y[j])
        max_y = max(max_y, y[j])

    area = (max_x - min_x) * (max_y - min_y)
    ans = min(ans, area)

print(ans)
