# 코드트리 Trail2. 개발자의 능력 3
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-ability-of-developer-3/description

abilities = list(map(int, input().split()))

# Please write your code here.
total = sum(abilities)
ans = float('inf')

for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            team1 = abilities[i] + abilities[j] + abilities[k]
            team2 = total - team1
            ans = min(ans, abs(team1 - team2))

print(ans)
