# 코드트리 Trail2. 선분 3개 지우기
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-remove-three-segments/description

n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

# Please write your code here.
MAX_X = 100
ans = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            line = [0] * (MAX_X + 1)
            for idx in range(n):
                if idx in (i, j, k):
                    continue
                for x in range(l[idx], r[idx] + 1):
                    line[x] += 1

            if all(cnt <= 1 for cnt in line):
                ans += 1

print(ans)
