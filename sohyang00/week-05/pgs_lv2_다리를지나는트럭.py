# 프로그래머스 Lv2. 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    current_weight = 0
    time = 0

    for truck in truck_weights:
        while True:
            time += 1
            current_weight -= bridge.popleft();

            if current_weight + truck <= weight:
                bridge.append(truck)
                current_weight += truck
                break
            else:
                bridge.append(0)
    return time + bridge_length

solution(100, 100,[10])
solution(100, 100,[10,10,10,10,10,10,10,10,10,10])
