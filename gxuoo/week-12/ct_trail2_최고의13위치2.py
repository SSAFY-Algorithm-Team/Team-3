# 코드트리 Trail2. 최고의 13위치 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-best-place-of-13-2/description

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def coins(i, j):
    return arr[i][j] + arr[i][j + 1] + arr[i][j + 2]

ans = 0
for i1 in range(n):
    for j1 in range(n - 2):
        for i2 in range(n):
            for j2 in range(n - 2):
                # 같은 행에서 3칸 이내로 시작하면 겹침
                if i1 == i2 and abs(j1 - j2) < 3:
                    continue
                ans = max(ans, coins(i1, j1) + coins(i2, j2))

print(ans)
