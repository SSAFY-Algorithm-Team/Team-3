# 코드트리 Trail2. 가운데에서 시작하여 빙빙 돌기
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-snail-start-from-center/description

n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
dxs = [0, -1, 0, 1]   # 오른쪽, 위, 왼쪽, 아래
dys = [1, 0, -1, 0]

x, y = n // 2, n // 2
grid[x][y] = 1
num = 2
idx = 0
length = 1

while num <= n * n:
    for _ in range(2):            # 같은 길이로 2방향 이동
        for _ in range(length):
            if num > n * n:       # 마지막 줄에서 격자 밖으로 나가지 않게
                break
            x += dxs[idx]
            y += dys[idx]
            grid[x][y] = num
            num += 1
        idx = (idx + 1) % 4
    length += 1

for row in grid:
    print(*row)
