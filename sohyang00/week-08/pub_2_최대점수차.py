# 기출 2. 최대 점수 차
# 소요시간:10m 시도횟수: 2

scores = [
    [1, 2],
    [2, 3],
    [3, 1],
    [4, 5],
    [2, 3],
    [1, 4]
]
#팀 번호, 획득 점수 

scores_curr = {}

for team, score in scores:
    if team not in scores_curr:
        scores_curr[team] = 0
    scores_curr[team] += score

max_score = -1
min_score = 10000
for team, score in scores_curr.items():
    if max_score < score:
        max_score = score
    if min_score > score:
        min_score = score

print(max_score - min_score)