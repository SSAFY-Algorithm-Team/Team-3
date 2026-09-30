def solution(actions):
    stop = 0
    done = 0
    drop = 0

    now_rank = None
    end_time = 0

    for order, rank, action in actions:

        # 현재 행동이 이미 끝난 경우
        if now_rank is not None and end_time <= order:
            done += 1
            now_rank = None

        # 현재 아무 행동도 안 하는 경우
        if now_rank is None:
            now_rank = rank
            end_time = order + action

        # 새 행동의 우선순위가 더 높은 경우
        elif rank < now_rank:
            stop += 1
            now_rank = rank
            end_time = order + action

        # 새 행동의 우선순위가 더 낮은 경우
        else:
            drop += 1

    # 마지막 행동은 끝까지 수행됨
    if now_rank is not None:
        done += 1

    return [stop, done, drop]