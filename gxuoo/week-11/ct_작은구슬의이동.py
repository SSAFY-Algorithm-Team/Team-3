# 코드트리. 작은 구슬의 이동
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-small-marble-movement/description

n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
def is_range(x, y):
    if 1 <= x <= n and 1 <= y <= n:
        return True

    return False

for i in range(t):
    if d == 'L':
        next_r, next_c = r, c - 1
        if is_range(next_r, next_c):
            r = next_r
            c = next_c
        else:
            d = 'R'
    elif d == 'R':
        next_r, next_c = r, c + 1
        if is_range(next_r, next_c):
            r = next_r
            c = next_c
        else:
            d = 'L'
    elif d == 'U':
        next_r, next_c = r - 1, c
        if is_range(next_r, next_c):
            r = next_r
            c = next_c
        else:
            d = 'D'
    else:
        next_r, next_c = r + 1, c
        if is_range(next_r, next_c):
            r = next_r
            c = next_c
        else:
            d = 'U'

print(r, c)
