# 코드트리 Trail2. 체크판위에서 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-on-the-checkboard-2/description

R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
cnt = 0
for i in range(1, R - 1):
    for j in range(1, C - 1):
        for k in range(i + 1, R - 1):
            for l in range(j + 1, C - 1):
                if (grid[0][0] != grid[i][j] and
                    grid[i][j] != grid[k][l] and
                    grid[k][l] != grid[R - 1][C - 1]):
                    cnt += 1

print(cnt)
