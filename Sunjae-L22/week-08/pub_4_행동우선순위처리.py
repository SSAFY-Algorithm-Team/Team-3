# 소요시간 : 20분

stopped = 0    # 중단된 행동 수
solved = 0     # 해결한 행동 수
discarded = 0  # 버린 행동 수

current_priority = None  
end_time = 0             

actions = [[0, 4, 5], [2, 1, 3], [3, 5, 2], [7, 2, 2]]

# 주문 시간순으로 처리
for order_time, priority, duration in sorted(actions, key=lambda x: x[0]):

    if current_priority is not None and end_time <= order_time:
        solved += 1
        current_priority = None

    # 1. 수행 중인 행동이 없으면 바로 시작
    if current_priority is None:
        current_priority = priority
        end_time = order_time + duration

    # 2. 새 행동의 우선순위가 더 높으면 기존 행동 중단 후 교체
    elif priority < current_priority:
        stopped += 1
        current_priority = priority
        end_time = order_time + duration

    # 3. 새 행동의 우선순위가 더 낮으면 새 행동을 버림
    else:
        discarded += 1

# 마지막 행동은 끝까지 수행
if current_priority is not None:
    solved += 1

print(stopped, solved, discarded)