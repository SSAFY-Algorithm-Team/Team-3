# 함정 피해 멀리 가기
# 시간복잡도: O(len(rolls) * n)

def solution(rolls, n):
    trap = n + 1

    # dp[i] :
    # 현재 위치를 trap으로 나눈 나머지가 i일 때
    # 도달 가능한 가장 먼 위치
    dp = [-1] * trap

    # 처음에는 0번 칸
    dp[0] = 0

    answer = 0

    for roll in rolls:
        # 이번 턴 이후 가능한 위치
        next_dp = [-1] * trap

        # 이번 턴에 그냥 0으로 돌아가는 선택
        next_dp[0] = 0

        for i in range(trap):
            # 도달할 수 없는 상태면 넘어감
            if dp[i] == -1:
                continue

            # 주사위만큼 이동
            next_pos = dp[i] + roll

            # 함정 칸에 도착하면 바로 0으로 돌아감
            if next_pos % trap == 0:
                next_dp[0] = 0

            else:
                # 현재 위치의 나머지
                remain = next_pos % trap

                # 같은 나머지라면 더 멀리 간 위치만 저장
                next_dp[remain] = max(
                    next_dp[remain],
                    next_pos
                )

                # 지금까지 도달한 안전 칸 중 최댓값
                answer = max(answer, next_pos)

        dp = next_dp

    return answer