# 프로그래머스 Lv2. 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 소요시간: 15분 / 시도: 1회


def solution(priorities, location):
    
    num = [i for i in range(len(priorities))] #고유 인덱스값 리스트로
    stack = []
    
    # 우선순위, 인덱스가 함께 들어갔다 나왔다
    while len(num) != 0:
        if priorities[0] >= max(priorities):
            
            #다시 보니까 그냥 인덱스값만 저장하고 location으로 위치만 반환해도 되네
            stack.append((priorities.pop(0),num.pop(0))) #인덱스값과 함께 저장
        else:
            priorities.append(priorities.pop(0))
            num.append(num.pop(0))
    
    for i in range(len(stack)):
        if stack[i][1] == location:
            return i+1  #순위는 1번부터니까


    
            
            
            
        
    


