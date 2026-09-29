# 기출 4. 행동 우선순위 처리
# 소요시간:10분 시도횟수: 2회

actions = [
[0, 4, 5],
[2, 1, 3],
[3, 5, 2],
[7, 2, 2]
]
# 주문시간, 우선순위, 행동시간

def sol(actions):
    stop = 0
    complete = 0
    drop = 0
    curr = [-1] * 3
    for action in actions:
        if curr[0] == -1:
            curr[0] = action[0]
            curr[1] = action[1]
            curr[2] = action[2]
            continue

        order = action[0]
        priority = action[1]
        execution = action[2]
        #현재 우선순위보다 새 작업의 우선순위가 높으면
        if priority > curr[1]:
            # 현재 작업이 끝났는지 확인
            if order - curr[0] >= curr[2]:
                complete += 1
            # 안 끝났으면 작업 중단
            else:
                stop += 1
            # 현재 작업을 새 작업으로 바꿈
            curr[0] = order
            curr[1] = priority
            curr[2] = execution
        # 현재 우선순위보다 새 행동의 우선순위가 낮으면
        else: 
            # 현재 작업이 끝났는지 확인
            if order - curr[0] >= curr[2]:
                complete += 1
            # 안 끝났으면 작업 중단
            else:
                drop += 1
            continue
    # 마지막 작업은 항상 완료가 가능하므로
    complete += 1
    result = []
    result.append([stop, complete, drop])
    return result

result = sol(actions)
print(result)

