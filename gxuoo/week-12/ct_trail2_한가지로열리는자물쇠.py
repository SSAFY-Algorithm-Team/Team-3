# 코드트리 Trail2. 한 가지로 열리는 자물쇠
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-one-way-lock/description

N = int(input())
a, b, c = map(int, input().split())

# Please write your code here.
cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if abs(i - a) <= 2 or abs(j - b) <= 2 or abs(k - c) <= 2:
                cnt += 1

print(cnt)
