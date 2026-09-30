# 기출 4: 행동 우선 순위 처리
# 소요시간: 30분 / 시도: 2회


#행동 수행 중 새로운 주문이 들어오면 다음 규칙을 따름
'''
새 행동이 우선순위 높으면 중단하고 새 행동 시작
중단되면 다시 하지 않음
새로운 행동의 우선순위가 더 낮으면 새로운 행동을 버림
'''

# 배열: [주문시간, 우선순위, 행동시간]
actions = [[0, 4, 5], [2, 1, 3], [3, 5, 2], [7, 2, 2]]
actions.sort()
# print(actions) sort 동작 확인용 / 혹시나 입력 배열이 무작위일 수 있으니

time = 0
process = []
stop, solve, drop = 0, 0, 0

# 남은 진행작업이 있을때까지 돌릴 필요가 있을까?
while actions:

    # 진행 작업이 없고, 주문시간과 맞으면 추가
    if not process:
        if time == actions[0][0]:
            process.append(actions.pop(0))
            #process[0][2] += time # 이렇게 진행하는 방식도 생각만해봄

    # 진행작업이 있음
    else:
        # 대기작업의 주문시간이 적으면
        if time >= actions[0][0]:

            # 기존 작업과 비교해서 유지 또는 교체
            if process[0][1] > actions[0][1]:
                process.pop()
                process.append(actions.pop(0))
                stop += 1

            else:
                actions.pop(0)
                drop += 1
    
    time += 1

    # 작업이 있을때 작업시간의 크기를 1씩 줄이기
    if process:
        process[0][2] -= 1 
        if process[0][2] == 0:
            process.pop()
            solve += 1

if not process:
    print([stop, solve, drop])  #정시에 딱 끝났을 수 있으니까

# 남은 작업은 무조건 수행하니까
else:
    print([stop, solve+1, drop]) #마지막 수행중인걸 위해 solve+1


