# 기출 4. 행동 우선순위 처리
# 소요시간: 10분 / 시도: 1회


def solution(actions):
    # [중단된 행동 수, 해결한 행동 수, 버린 행동 수]
    answer = [0, 0, 0]

    stop, solve, drop = 0, 0, 0
    cur_priority, end_time = None, None

    for order, priority, action in actions:
        # 기존 행동이 새로운 행동 전에 끝났을 때
        if cur_priority is not None and end_time <= order:
            solve += 1
            cur_priority = None
            end_time = None
 
        # 수행 중인 행동 없으면 시작
        if cur_priority is None:
            cur_priority = priority
            end_time = order + action
            continue
        
        # 우선 순위는 숫자 작은 순서로
        if priority < cur_priority:
            stop += 1
            cur_priority = priority
            end_time = order + action
        else:
            drop += 1

    # 마지막 행동은 끝까지 진행
    if cur_priority is not None:
        solve += 1

    answer = [stop, solve, drop]
    return answer


if __name__ == "__main__":
    # [주문 시간, 우선순위, 행동 시간]
    print(solution([
        [0, 4, 5], 
        [2, 1, 3],
        [3, 5, 2], 
        [7, 2, 2]
    ]))  # [1, 2, 1]
