# 코드트리 Trail2. 오목
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-O-mok/description

board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
dxs = [0, 1, 1, -1]
dys = [1, 0, 1, 1]

def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

def is_win(r, c, dx, dy):
    color = board[r][c]
    for i in range(5):
        nx, ny = r + dx * i, c + dy * i
        if not in_range(nx, ny) or board[nx][ny] != color:
            return False
    return True

def solve():
    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:
                continue
            for dx, dy in zip(dxs, dys):
                if is_win(i, j, dx, dy):
                    # 가운데 돌 = 시작점에서 2칸 이동, 1-indexed로 출력
                    print(board[i][j])
                    print(i + 2 * dx + 1, j + 2 * dy + 1)
                    return
    print(0)

solve()
