# 프로그래머스 Lv2. 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    waiting = deque(truck_weights)
    bridge = deque()

    time = 0
    current_weight = 0

    while waiting or bridge:
        time += 1

        # 1. 다리를 모두 건넌 트럭 제거
        if bridge and bridge[0][1] + bridge_length == time:
            truck_weight, enter_time = bridge.popleft()
            current_weight -= truck_weight

        # 2. 다음 트럭이 무게 제한을 만족하면 다리에 올림
        if waiting and current_weight + waiting[0] <= weight:
            truck_weight = waiting.popleft()
            bridge.append((truck_weight, time))
            current_weight += truck_weight

    return time