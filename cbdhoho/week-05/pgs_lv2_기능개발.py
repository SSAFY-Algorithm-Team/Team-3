def solution(progresses, speeds):
    answer = [1]
    days = []
    for p, s in zip(progresses, speeds):
        day = 1
        # progress에 speed를 더해가면서 100 넘으면 스탑
        while p + s*day < 100:
            day += 1
        # 걸린 날 days 배열에 추가
        days.append(day)
    # 기준이 되는 날
    max_day = days[0]
    for i in range(1, len(days)):
        # max_day보다 작으면 배포 나중에 해야되니까 answer 마지막 값에 +1
        if days[i] <= max_day:
            answer[-1] += 1
        # max_day보다 크면 배포 바로 해도되니까, answer에 1 append
        else:
            max_day = days[i]
            answer.append(1)
    return answer