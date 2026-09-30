# 기출 2: 최대 점수 차
# 소요시간: 20분 / 시도: 1회

scores = [
    [1,2],
    [2,3],
    [3,1],
    [4,5],
    [2,3],
    [1,4]
]

# 몇 팀이나 있는지 체크
check_team = set(scores[i][0] for i in range(len(scores)))

# 체크된 만큼 팀 생성
team_scores = [0 for _ in range(len(check_team))]

# 팀 인덱스에 맞게 점수 합산
for score in scores:
    i, j = score

    team_scores[i-1] += j

#(최대-최소)로 최솟값 구하기
print(max(team_scores)- min(team_scores))
