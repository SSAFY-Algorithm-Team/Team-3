# 프로그래머스 Lv3. 디스크 컨트롤러
# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 소요시간: 35분 / 시도: 4회

import heapq

def solution(jobs):
    min_heap = []           # 디스크 대기 큐 정의
    answer = 0              # 각 작업 반환 시간의 총합
    current_time = 0        # 현재 시각
    idx = 0                 # 아직 대기 큐에 넣지 않은 작업의 위치
    done = 0                # 완료한 작업 수

    # 작업 요청 순서로 정렬
    jobs.sort(key=lambda x: x[0])
    
    while done < len(jobs):
        # 1) 현재 시각까지 요청된 작업을 전부 대기 큐로 옮긴다
        while idx < len(jobs) and jobs[idx][0] <= current_time:
            request_time, running_time = jobs[idx]
            heapq.heappush(min_heap, (running_time, request_time, idx))
            idx += 1

        # 2) 대기 큐에서 우선순위가 가장 높은 작업 실행
        if min_heap:
            running_time, request_time, _ = heapq.heappop(min_heap)
            current_time += running_time
            answer += current_time - request_time
            done += 1
        # 3) 대기 큐가 비었다
        else:
            # 다음 작업이 요청되는 시각으로 시간을 건너뛴다
            current_time = jobs[idx][0]
    
    return answer // len(jobs)
