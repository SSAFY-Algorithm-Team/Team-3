# 함정피해 멀리 가기
# 소요시간 : 60분

# 시간초과났을듯?
def solution(rolls, n):
    answer = 0
    trap = n + 1

    for start in range(len(rolls)):
        position = 0

        for i in range(start, len(rolls)):
            position += rolls[i]

            if position % trap == 0:
                break

            answer = max(answer, position)

    return answer


# DP 풀이
def solution(rolls, n):
    trap = n + 1

    # dp[r]: 현재 턴까지 처리한 후,
    # 나머지가 r인 도달 가능 위치 중 최댓값
    # -1은 도달 불가능
    dp = [-1] * trap
    dp[0] = 0

    answer = 0

    for roll in rolls:
        next_dp = [-1] * trap

        # 이번 턴에 출발점으로 돌아가는 선택
        next_dp[0] = 0

        for remainder in range(trap):
            position = dp[remainder]

            if position == -1:
                continue

            next_position = position + roll
            next_remainder = next_position % trap

            # 함정에 도착하면 0으로 돌아간다.
            # next_dp[0]에 이미 반영되어 있음.
            if next_remainder == 0:
                continue

            next_dp[next_remainder] = max(
                next_dp[next_remainder],
                next_position
            )

            answer = max(answer, next_position)

        dp = next_dp

    return answer