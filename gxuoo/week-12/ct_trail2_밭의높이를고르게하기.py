# 코드트리 Trail2. 밭의 높이를 고르게하기
# https://www.codetree.ai/ko/trails/complete/curated-cards/test-equalizing-the-height-of-the-field/description

N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
ans = float('inf')
for i in range(N - T + 1):
    cost = sum(abs(h - H) for h in arr[i:i + T])
    ans = min(ans, cost)

print(ans)
