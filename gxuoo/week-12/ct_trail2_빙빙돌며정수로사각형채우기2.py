# 코드트리 Trail2. 빙빙 돌며 정수로 사각형 채우기 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-snail-number-square-2/description

n, m = map(int, input().split())

# Please write your code here.
arr = [[0] * m for _ in range(n)]

dxs = [1, 0, -1, 0]   # 아래, 오른쪽, 위, 왼쪽 (반시계 방향)
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

x, y = 0, 0
idx = 0
arr[x][y] = 1

for num in range(2, n * m + 1):
    nx, ny = x + dxs[idx], y + dys[idx]
    # 막히면 다음 방향으로 회전
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        idx = (idx + 1) % 4
        nx, ny = x + dxs[idx], y + dys[idx]
    x, y = nx, ny
    arr[x][y] = num

for row in arr:
    print(*row)
    