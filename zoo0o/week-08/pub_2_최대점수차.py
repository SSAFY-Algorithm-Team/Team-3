def solution(scores):
    team = {}

    # 등장하는 모든 팀을 0점으로 초기화
    for num, score in scores:
        team[num] = 0

    answer = 0

    for num, score in scores:
        team[num] += score

        diff = max(team.values()) - min(team.values())
        answer = max(answer, diff)

    return answer