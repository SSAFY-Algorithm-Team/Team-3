# 코드트리 Trail2. 거울에 레이저 쏘기 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-shoot-a-laser-in-the-mirror-2/description

n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
dxs = [-1, 0, 1, 0]   # 0: 위, 1: 오른쪽, 2: 아래, 3: 왼쪽
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 시작 위치와 방향
if k <= n:
    x, y, d = 0, k - 1, 2
elif k <= 2 * n:
    x, y, d = k - n - 1, n - 1, 3
elif k <= 3 * n:
    x, y, d = n - 1, 3 * n - k, 0
else:
    x, y, d = 4 * n - k, 0, 1

cnt = 0
while in_range(x, y):
    if grid[x][y] == '/':
        d = d ^ 1
    else:  # '\'
        d = 3 - d
    cnt += 1
    x, y = x + dxs[d], y + dys[d]

print(cnt)
