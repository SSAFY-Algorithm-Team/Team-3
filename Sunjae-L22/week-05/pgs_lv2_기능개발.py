# 프로그래머스 Lv2. 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 소요시간: 10분 / 시도: 1회

def solution(progresses, speeds):
    progress_n = len(progresses)
    work_day = [0] * progress_n
    for i in range(progress_n):
        if (100 - progresses[i]) % speeds[i] == 0:
            work_day[i] = (100 - progresses[i]) // speeds[i]
        else:
            work_day[i] = (100 - progresses[i]) // speeds[i] + 1
    # [5, 10, 1, 1, 20, 1] -> [1, 3, 2]
    answer = []
    cnt = 0
    last = work_day[0]
    for day in work_day:
        if day > last:
            answer.append(cnt)
            cnt = 0
            last = day
        cnt += 1
    answer.append(cnt)

    return answer