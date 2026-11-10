# 코드트리. 되돌아오기
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-come-back/description

N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
delta = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

x, y = 0, 0
time = 0
ans = -1

for d, k in zip(dir, dist):
    dx, dy = delta[d]
    for _ in range(k):
        x += dx
        y += dy
        time += 1
        if x == 0 and y == 0:
            ans = time
            break
    if ans != -1:   # 안쪽 break만으로는 바깥 루프가 계속 돎
        break

print(ans)
