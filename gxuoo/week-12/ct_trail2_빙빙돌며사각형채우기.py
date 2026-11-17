# 코드트리 Trail2. 빙빙 돌며 사각형 채우기
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-snail-alphabet-square/description

n, m = map(int, input().split())

# Please write your code here.
arr = [[''] * m for _ in range(n)]

dxs = [0, 1, 0, -1]   # 오른쪽, 아래, 왼쪽, 위 (시계 방향)
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

x, y = 0, 0
idx = 0
arr[x][y] = 'A'

for i in range(1, n * m):
    nx, ny = x + dxs[idx], y + dys[idx]
    if not in_range(nx, ny) or arr[nx][ny] != '':
        idx = (idx + 1) % 4
        nx, ny = x + dxs[idx], y + dys[idx]
    x, y = nx, ny
    arr[x][y] = chr(ord('A') + i % 26)   # Z 다음은 다시 A

for row in arr:
    print(*row)
    