# 2115. [모의 SW 역량테스트] 벌꿀채취
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu&
# AI

T = int(input())


# M개의 벌통에서 얻을 수 있는 최대 수익 계산
def get_max_profit(honey, C):
    M = len(honey)
    max_profit = 0

    def dfs(idx, honey_sum, profit):
        nonlocal max_profit

        # 채취량이 C를 넘으면 불가능
        if honey_sum > C:
            return

        # M개의 벌통을 모두 확인한 경우
        if idx == M:
            max_profit = max(max_profit, profit)
            return

        # 현재 벌통의 꿀을 채취하는 경우
        dfs(
            idx + 1,
            honey_sum + honey[idx],
            profit + honey[idx] ** 2
        )

        # 현재 벌통의 꿀을 채취하지 않는 경우
        dfs(
            idx + 1,
            honey_sum,
            profit
        )

    dfs(0, 0, 0)

    return max_profit


for tc in range(1, T + 1):

    # N: 벌통의 크기
    # M: 선택해야 하는 연속된 벌통의 개수
    # C: 한 일꾼이 채취할 수 있는 최대 꿀의 양
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # (행, 시작 열, 해당 구간의 최대 수익)
    sections = []

    # 가로로 연속된 M개의 모든 구간 확인
    for i in range(N):
        for j in range(N - M + 1):
            honey = arr[i][j:j + M]
            profit = get_max_profit(honey, C)

            sections.append((i, j, profit))

    answer = 0

    # sections에서 겹치지 않는 구간 2개 선택
    for i in range(len(sections)):
        row1, col1, profit1 = sections[i]

        for j in range(i + 1, len(sections)):
            row2, col2, profit2 = sections[j]

            # 같은 행에서 두 구간이 겹치는 경우
            if row1 == row2 and col1 + M > col2:
                continue

            answer = max(answer, profit1 + profit2)

    print(f'#{tc} {answer}')