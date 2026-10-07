# 복기 3. 함정 피해 멀리 가기
# 소요시간: 45분 / 시도: 5회

# def solution(rolls, n):
#     # 함정: n+1의 배수. 0은 함정이 아님
#     pitfall = n + 1
#     m = len(rolls)
#     best = 0
#
#     def dfs(index, pos):
#         nonlocal best
#         # best 갱신
#         best = max(best, pos)
#
#         # 종료 조건
#         if index == m:
#             return best
#
#         # 분기 1 - 이동 (함정이면 0으로)
#         next_pos = pos + rolls[index]
#         if not next_pos % pitfall:
#             dfs(index + 1, 0)
#         else:
#             dfs(index + 1, next_pos)
#
#         # 분기 2 - 리셋
#         dfs(index + 1, 0)
#
#     dfs(0, 0)
#     return best

def solution(rolls, n):
    P = n + 1
    m = len(rolls)

    # reach_next[r] = max_reach(turn + 1, r)
    # 처음엔 turn = m 이라 전부 0
    reach_next = [0] * P
    best = 0

    for turn in range(m - 1, -1, -1):
        # reach_now[r] = max_reach(turn, r)
        reach_now = [0] * P          
        for remainder in range(P):
            next_remainder = (remainder + rolls[turn]) % P
            if next_remainder == 0:
                # 이동하면 함정
                reach_now[remainder] = 0                      
            else:
                reach_now[remainder] = rolls[turn] + reach_next[next_remainder]

        # turn번 턴에서 0번 칸부터 새로 출발했을 때
        best = max(best, reach_now[0])

        reach_next = reach_now

    return best


if __name__ == "__main__":
    print(solution([2, 3, 4, 2, 2], 4))  # 11
    print(solution([2, 2, 2], 2))  # 4
    print(solution([3, 1, 4, 1, 5, 2, 6, 5, 3, 5], 6))  # 32
