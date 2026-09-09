# 프로그래머스 Lv3. 디스크 컨트롤러
# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 소요시간: 25분 / 시도: 1회

import heapq

# 우선순위 : 소요시간 짧은 것, 요청 시간이 빠른 것, 번호작은것 순

def solution(jobs):
    arr = sorted((s, l, i) for i, (s, l) in enumerate(jobs))
    job_n = len(arr)
    h = []
    idx = now = total = done = 0

    # s : 작업 요청 시점
    # l : 작업 소요시간
    while done < job_n:
        # 현재시각보다 요청 시간이 이전이라면, 힙에 넣어준다(우선순위대로)
        while idx < job_n and arr[idx][0] <= now:
            s, l, i = arr[idx]
            heapq.heappush(h, (l, s, i))
            idx += 1

        # 만약 대기 큐가 비어있지 않다면 즉시 작업 시작
        if h:
            l, s, i = heapq.heappop(h)
            now += l
            # total에 요청부터 종료까지 시간 더해주기
            total += now - s
            done += 1
        else:
            now = arr[idx][0]   # 놀고 있으면 다음 요청까지 점프

    return total // job_n