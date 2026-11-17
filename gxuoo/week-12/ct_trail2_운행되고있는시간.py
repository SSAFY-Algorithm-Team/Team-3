# 코드트리 Trail2. 운행 되고 있는 시간
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-hours-in-service/description

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.
MAX_T = 1000
ans = 0
for fired in range(n):
    timeline = [0] * (MAX_T + 1)
    for i in range(n):
        if i == fired:
            continue
        for t in range(a[i], b[i]):
            timeline[t] += 1

    covered = sum(1 for cnt in timeline if cnt >= 1)
    ans = max(ans, covered)

print(ans)
