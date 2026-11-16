# 코드트리 Trail2. G or H 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-G-or-H-2/description

n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
MAX_POS = 100
arr = [''] * (MAX_POS + 1)
for p, a in zip(pos, alpha):
    arr[p] = a

ans = 0
for i in range(MAX_POS + 1):
    if arr[i] == '':
        continue
    for j in range(i, MAX_POS + 1):
        if arr[j] == '':
            continue
        part = arr[i:j + 1]
        g = part.count('G')
        h = part.count('H')
        if g == 0 or h == 0 or g == h:
            ans = max(ans, j - i)

print(ans)
