# 코드트리 Trail2. G or H 3
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-G-or-H-3/description

n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
arr = [0] * 10001
for i in range(n):
    arr[x[i]] = 1 if c[i] == 'G' else 2

ans = 0
for i in range(1, max(1, 10000 - k) + 1):
    ans = max(ans, sum(arr[i:i + k + 1]))

print(ans)
