# swea [모의 SW 역량테스트] 벌꿀채취
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
# 소요시간: 45분 / 시도: 2회

# 2115. 벌꿀채취

def gain_honey(N, honey_map, M, C):
    # 선택한 M개 벌통에서 얻을 수 있는 최대 수익, honeys : M개 
    def get_profit(honeys):
        best = 0

        # amount : 꿀 양, profit : 제곱해서 합한 꿀 가치
        def dfs(idx, amount, profit):
            nonlocal best

            if amount > C:
                return

            if idx == M:
                best = max(best, profit)
                return

            # 현재 벌통에서 채취하지 않는 경우
            dfs(idx + 1, amount, profit)

            # 현재 벌통에서 채취하는 경우
            honey = honeys[idx]
            dfs(idx + 1, amount + honey, profit + honey * honey)

        dfs(0, 0, 0)
        return best

    # 각 구간의 (행, 시작 열, 최대 수익) 저장
    candidates = []

    for r in range(N):
        for c in range(N - M + 1):
            honeys = honey_map[r][c:c + M]
            profit = get_profit(honeys)
            candidates.append((r, c, profit))

    answer = 0

    # 두 일꾼이 선택할 구간 비교
    for i in range(len(candidates)):
        r1, c1, profit1 = candidates[i]

        for j in range(i + 1, len(candidates)):
            r2, c2, profit2 = candidates[j]

            # 같은 행 / 구간이 겹치면 선택 불가능
            if r1 == r2 and c1 + M > c2:
                continue

            answer = max(answer, profit1 + profit2)

    return answer


T = int(input())

for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())

    honey_map = []
    for i in range(N):
        honey_map.append(list(map(int, input().split())))

    answer = gain_honey(N, honey_map, M, C)
    print(f"#{test_case} {answer}")