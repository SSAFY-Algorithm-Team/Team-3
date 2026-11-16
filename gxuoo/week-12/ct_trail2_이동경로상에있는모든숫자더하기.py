# 코드트리 Trail2. 이동경로상에 있는 모든 숫자 더하기
# https://www.codetree.ai/ko/trails/complete/curated-cards/test-add-all-the-numbers-on-the-path/description

N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
dxs = [-1, 0, 1, 0]   # 북, 동, 남, 서 (시계 방향)
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

x, y = N // 2, N // 2
idx = 0                # 북쪽
total = board[x][y]    # 시작 칸 포함

for c in str:
    if c == 'L':
        idx = (idx - 1) % 4
    elif c == 'R':
        idx = (idx + 1) % 4
    else:  # F
        nx, ny = x + dxs[idx], y + dys[idx]
        if in_range(nx, ny):
            x, y = nx, ny
            total += board[x][y]

print(total)
