# 프로그래머스 Lv2. 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 소요시간: 20분 / 시도: 3회

import math

def solution(progresses, speeds):
    complete = []
    answer = []

    # 1. 각 기능이 완료되기까지 필요한 일수 계산
    for i in range(len(progresses)):
        complete.append(math.ceil((100 - progresses[i]) / speeds[i] ))

    # 2. 첫 번째 기능의 완료일을 현재 배포 기준일로 설정
    current = complete[0]
    count = 0

    # 3. 기준일 안에 완료되는 기능은 같은 배포에 포함
    for cmp in complete:
        if current >= cmp:
            count += 1

        # 4. 더 늦게 완료되는 기능을 만나면 이전 배포 묶음 저장
        elif current < cmp:
            answer.append(count)
            count = 1
            current = cmp

    # 5. 마지막 배포 묶음 추가
    answer.append(count)

    return answer