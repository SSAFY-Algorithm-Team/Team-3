# 프로그래머스 Lv3. 디스크 컨트롤러
# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    # 작업 번호를 붙이고 요청시간 순으로 정렬
    jobs = [(start, length, idx) for idx, (start, length) in enumerate(jobs)]
    jobs.sort()

    waiting = []        # 대기 큐
    now = 0             # 현재 시간
    total = 0           # 반환 시간의 총합
    idx = 0             # jobs에서 확인할 작업 위치
    count = len(jobs)

    while idx < count or waiting:

        # 현재 시간까지 요청된 작업을 모두 대기 큐에 추가
        while idx < count and jobs[idx][0] <= now:
            start, length, job_num = jobs[idx]

            # 우선순위: 소요시간 → 요청시간 → 작업번호
            heapq.heappush(waiting, (length, start, job_num))
            idx += 1

        # 대기 중인 작업이 있으면 가장 우선순위가 높은 작업 실행
        if waiting:
            length, start, job_num = heapq.heappop(waiting)

            now += length
            total += now - start

        # 대기 큐가 비었다면 다음 작업의 요청시간으로 이동
        else:
            now = jobs[idx][0]

    return total // count