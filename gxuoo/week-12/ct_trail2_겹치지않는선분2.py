# 코드트리 Trail2. 겹치지 않는 선분 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-line-segments-that-do-not-overlap-2/description

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
overlap = [False] * n
for i in range(n):
    for j in range(i + 1, n):
        ax1, ax2 = lines[i]
        bx1, bx2 = lines[j]
        # 위아래 순서가 뒤바뀌면 교차
        if (ax1 - bx1) * (ax2 - bx2) < 0:
            overlap[i] = True
            overlap[j] = True

print(overlap.count(False))
