# 코드트리 Trail2. 두 가지로 열리는 자물쇠
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-a-two-way-lock/description

N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
def close(x, y):
    d = abs(x - y)
    return min(d, N - d) <= 2

cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            ok1 = close(i, a1) and close(j, b1) and close(k, c1)
            ok2 = close(i, a2) and close(j, b2) and close(k, c2)
            if ok1 or ok2:
                cnt += 1

print(cnt)
