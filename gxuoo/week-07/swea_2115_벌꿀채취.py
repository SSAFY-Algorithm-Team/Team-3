# SWEA 2115. [모의 SW 역량테스트] 벌꿀채취
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu
# 소요시간: / 시도:


'''
으으 다시 풀어야 함....
나 DFS 어떻게 풀었는지 기억도 안 나 으으...
추석 연휴 때 연습 많이 해올게요....
'''


def best_profit(cells, limit):
    """길이 M짜리 구간 cells에서 합이 limit 이하가 되게 골랐을 때의 최대 제곱합.

    각 칸을 '담는다 / 안 담는다'로 나누는 DFS.
    - 담았을 때 합이 limit을 넘으면 그 가지는 버린다
    - 끝까지 갔으면 지금까지의 제곱합을 최댓값과 비교
    """
    best = 0

    def dfs(idx, total, score):
        nonlocal best
        if idx == len(cells):
            best = max(best, score)
            return

        # 담는다 (합이 limit을 넘지 않을 때만)
        if total + cells[idx] <= limit:
            dfs(idx + 1, total + cells[idx], score + cells[idx] ** 2)

        # 안 담는다
        dfs(idx + 1, total, score)

    dfs(0, 0, 0)
    return best


def solve(n, m, c, board):
    # 1단계: 모든 (행, 시작열) 구간의 최대 수익을 미리 구해둔다
    #        시작열은 0 ~ n-m (n-m 포함)
    profit = [[0] * (n - m + 1) for _ in range(n)]
    for r in range(n):
        for start in range(n - m + 1):
            profit[r][start] = best_profit(board[r][start:start + m], c)

    # 2단계: 겹치지 않는 두 구간의 합 중 최댓값
    #        행이 다르면 OK / 행이 같으면 시작열 차이가 m 이상이어야 OK
    answer = 0
    for r1 in range(n):
        for c1 in range(n - m + 1):
            for r2 in range(n):
                for c2 in range(n - m + 1):
                    if r1 == r2 and abs(c1 - c2) < m:
                        continue
                    answer = max(answer, profit[r1][c1] + profit[r2][c2])
    return answer


T = int(input())
for tc in range(1, T + 1):
    n, m, c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    print(f"#{tc} {solve(n, m, c, board)}")
