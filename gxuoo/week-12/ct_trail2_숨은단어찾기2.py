# 코드트리 Trail2. 숨은 단어 찾기 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-find-hidden-words-2/description

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
dxs = [-1, -1, -1, 0, 0, 1, 1, 1]
dys = [-1, 0, 1, -1, 1, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != 'L':
            continue
        for dx, dy in zip(dxs, dys):
            x1, y1 = i + dx, j + dy
            x2, y2 = i + 2 * dx, j + 2 * dy
            if (in_range(x2, y2) and arr[x1][y1] == 'E' and arr[x2][y2] == 'E'):
                cnt += 1

print(cnt)
