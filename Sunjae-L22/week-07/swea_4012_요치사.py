# swea [모의 SW 역량테스트] 요리사
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
# 소요시간: 25분 / 시도: 2회

from itertools import combinations

T = int(input())


def score(sinergy, ingredients):
    n = len(ingredients)
    score = 0
    for i in range(n):
        for j in range(i+1, n):
            score += sinergy[ingredients[i]][ingredients[j]]
            score += sinergy[ingredients[j]][ingredients[i]]
    return score


for test_case in range(1, T + 1):
    N = int(input())
    sinergy = []
    taste_diff = 999999999

    for i in range(N):
        sinergy.append(list(map(int, input().split())))

    for comb in combinations(range(N), N//2):
        group1, group2 = [], []

        for i in range(N):
            if i in comb:
                group1.append(i)
            else:
                group2.append(i)

        taste_diff = min(taste_diff, abs(score(sinergy, group1) - score(sinergy, group2)))

    print(f"#{test_case} {taste_diff}")