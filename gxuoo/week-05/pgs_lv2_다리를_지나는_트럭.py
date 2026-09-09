# 프로그래머스 Lv2. 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 소요시간: 25분 / 시도: 1회

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)   # 다리를 길이만큼의 칸으로
    trucks = deque(truck_weights)
    time = 0
    on_bridge = 0
    
    while trucks:
        time += 1
        on_bridge -= bridge.popleft()      # 한 칸 전진, 맨 앞 칸이 빠져나감

        if on_bridge + trucks[0] <= weight:
            next_truck = trucks.popleft()
            bridge.append(next_truck)
            on_bridge += next_truck
        else:
            bridge.append(0)               # 못 들어가면 빈 칸

    # 마지막 트럭이 다리를 다 건너는 시간을 더함
    time += bridge_length

    return time
