# 코드트리. 빙빙 돌며 수로 직사각형 채우기
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-snail-number-square/description

n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
dxs = [0, 1, 0, -1]   # R, D, L, U 순서 (시계 방향)
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

x, y = 0, 0
idx = 0
arr[x][y] = 1

for num in range(2, n * m + 1):
    nx, ny = x + dxs[idx], y + dys[idx]
    # 막히면 시계 방향 회전
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        idx = (idx + 1) % 4
        nx, ny = x + dxs[idx], y + dys[idx]
    x, y = nx, ny
    arr[x][y] = num

for row in arr:
    print(*row)
