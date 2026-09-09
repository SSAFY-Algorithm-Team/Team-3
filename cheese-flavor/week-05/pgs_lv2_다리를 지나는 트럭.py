# 프로그래머스 Lv2. 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 소요시간: 50분 / 시도: 4회


from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 그냥 리스트 하나 deque를 쓰나 로직은 같고 속도차이만

    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    time = 0
    
    truck_weights = deque(truck_weights)
    total_trucks = len(truck_weights)
    passed = 0 #통과한 차량수
    
       
    while passed < total_trucks:
        time += 1
        
        out_truck = bridge.popleft() #인덱스 0에 있는걸 뺌
        bridge_weight -= out_truck 
        
        if out_truck != 0:
            passed += 1  # 다리를 완전히 건넌 트럭 카운트
        
        #남아있는 트럭이 있다면
        if truck_weights:
            next_truck = truck_weights[0]
            
            #무게보다 낮으면 추가하고 다리 무게도 추가
            if bridge_weight + next_truck <= weight:
                truck_weights.popleft()
                bridge_weight += next_truck
                bridge.append(next_truck)
             
            else:
                bridge.append(0) #무게 안되면 0 추가
                
        else:
            bridge.append(0) #남은 트럭없어도 0 추가
    
    return time


    
            
            
            
        
    


