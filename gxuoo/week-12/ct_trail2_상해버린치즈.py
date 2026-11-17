# 코드트리 Trail2. 상해버린 치즈
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-rotten-cheese/description

N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# Please write your code here.
ans = 0

for cheese in range(1, M + 1):   # 치즈 cheese가 상했다고 가정
    # 1단계: 아픈 사람 전원이 아프기 전에 이 치즈를 먹었는지 확인
    possible = True
    for i in range(S):
        ate_before = False
        for j in range(D):
            # 같은 사람이, 이 치즈를, 아프기 전에 먹었는지
            if p[j] == sick_p[i] and m[j] == cheese and t[j] < sick_t[i]:
                ate_before = True
                break
        if not ate_before:      # 한 명이라도 설명이 안 되면
            possible = False    # 이 치즈는 상한 치즈가 아님
            break

    if not possible:
        continue

    # 2단계: 이 치즈를 먹은 사람 수 세기 (같은 사람 중복 제거)
    ate = [False] * (N + 1)
    for j in range(D):
        if m[j] == cheese:
            ate[p[j]] = True

    cnt = 0
    for person in range(1, N + 1):
        if ate[person]:
            cnt += 1

    ans = max(ans, cnt)

print(ans)
