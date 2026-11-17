# 코드트리 Trail2. 등차수열
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-arithmetic-sequence/description

n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
ans = 0
for k in range(1, 101):
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] == 2 * k:
                cnt += 1
    ans = max(ans, cnt)

print(ans)
