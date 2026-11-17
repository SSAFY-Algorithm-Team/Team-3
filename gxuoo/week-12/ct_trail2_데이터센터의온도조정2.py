# 코드트리 Trail2. 데이터센터의 온도 조정 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-adjusting-the-temperature-of-the-data-center-2/description

N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
MAX_T = 1000
ans = 0
for temp in range(-1, MAX_T + 2):   # -1 ~ 1001
    total = 0
    for ta, tb in ranges:
        if temp < ta:
            total += C
        elif temp <= tb:
            total += G
        else:
            total += H
    ans = max(ans, total)

print(ans)