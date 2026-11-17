# 코드트리 Trail2. 개발자의 능력 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-ability-of-developer-2/description

ability = list(map(int, input().split()))

# Please write your code here.
ability.sort()
res = []
for i in range(3):
    res.append(ability[i] + ability[5 - i])


print(max(res) - min(res))
