# 코드트리. 격자 위의 편안한 상태
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-comfortable-state-on-the-grid/description

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
grid = [[0] * n for _ in range(n)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for r, c in points:
    x, y = r - 1, c - 1   # 입력은 1-indexed
    grid[x][y] = 1

    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt += 1

    print(1 if cnt == 3 else 0)
