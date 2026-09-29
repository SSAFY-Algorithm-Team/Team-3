# 소요시간 : 10분

from collections import defaultdict

scores = [[1, 2], [2, 3], [3, 1], [4, 5], [2, 3], [1, 4]]

# 일단 팀 찾기(초기 점수는 0)
team_score = defaultdict()
for team, _ in scores:
    team_score[team] = 0

# 득점마다 점수차 제일 큰게 있나 갱신
max_diff = 0
for team, score in scores:
    team_score[team] += score
    max_diff = max(max_diff, max(team_score.values()) - min(team_score.values()))

print(max_diff)