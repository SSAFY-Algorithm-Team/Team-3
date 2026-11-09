# 코드트리. 되돌아오기 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-come-back-2/description

commands = input()

# Please write your code here.
dxs = [0, 1, 0, -1]   # 북, 동, 남, 서 (시계 방향)
dys = [1, 0, -1, 0]

x, y = 0, 0
idx = 0
ans = -1

for i, c in enumerate(commands):
    if c == 'L':
        idx = (idx - 1) % 4
    elif c == 'R':
        idx = (idx + 1) % 4
    else:  # F
        x += dxs[idx]
        y += dys[idx]

    if x == 0 and y == 0:
        ans = i + 1   # L, R도 1초씩 걸리므로 순번 = 시간
        break

print(ans)
