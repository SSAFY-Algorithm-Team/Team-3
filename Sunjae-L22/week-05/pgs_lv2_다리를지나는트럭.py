# 프로그래머스 Lv2. 다리를지나는트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 소요시간: 30분 / 시도: 2회

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    now_weight = 0
    on_bridge = deque()

    while truck_weights or on_bridge:
        answer += 1
        for t in on_bridge:                  # 먼저 진행
            t[0] += 1
        while on_bridge and on_bridge[0][0] == bridge_length:
            now_weight -= on_bridge.popleft()[1]   # 무게 빼기!
        if truck_weights and now_weight + truck_weights[0] <= weight:
            t = truck_weights.popleft()
            now_weight += t
            on_bridge.append([0, t])
    return answer