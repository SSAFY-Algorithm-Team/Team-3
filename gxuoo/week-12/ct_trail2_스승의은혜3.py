# 코드트리 Trail2. 스승의 은혜 3
# https://www.codetree.ai/ko/trails/complete/curated-cards/test-the-grace-form-teacher-3/description

N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.
ans = 0

for i in range(N):
    # 학생별 실제 비용 = 가격 + 배송비 (i번만 가격 절반)
    costs = [P[j] + S[j] for j in range(N)]
    costs[i] = P[i] // 2 + S[i]
    costs.sort()

    total, cnt = 0, 0
    for c in costs:
        if total + c <= B:
            total += c
            cnt += 1
        else:
            break

    ans = max(ans, cnt)

print(ans)
