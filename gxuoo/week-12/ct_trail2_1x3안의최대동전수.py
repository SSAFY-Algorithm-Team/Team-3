# 코드트리 Trail2. 1x3 안의 최대 동전 수
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-best-place-of-13/description

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(n):
    for j in range(n - 2):   # 가로 3칸이 격자 안에 들어오는 시작 열
        cnt = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        ans = max(ans, cnt)

print(ans)
