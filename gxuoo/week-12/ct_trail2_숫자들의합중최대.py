# 코드트리 Trail2. 숫자들의 합 중 최대
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-maximum-of-sum-of-numbers/description

X, Y = map(int, input().split())

# Please write your code here.
ans = 0
for i in range(X, Y + 1):
    num = i
    res = 0
    while num:
        res += num % 10
        num //= 10

    ans = max(ans, res)

print(ans)
