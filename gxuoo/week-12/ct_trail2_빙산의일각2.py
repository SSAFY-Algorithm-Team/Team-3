# 코드트리 Trail2. 빙산의 일각 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-the-tip-of-the-iceberg-2/description

n = int(input())
h = [int(input()) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(max(h) + 1):
    arr = [0] * n
    for j in range(n):
        if h[j] > i:
            arr[j] = h[j] - i
        else:
            arr[j] = 0

    cnt = 0
    for j in range(n):
        if arr[j] > 0 and (j == 0 or arr[j - 1] == 0):
            cnt += 1

    ans = max(ans, cnt)

print(ans)
