# SWEA 2115. 벌꿀채취
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do
# 소요시간: 180분 / 시도: 4회


#구조적으로 어떻게 구성하지를 먼저 생각해야할듯?
#시간을 너무 많이 써먹고 흐름이 잘 안잡힘 ;;

from itertools import combinations

def get_profit(honey, C):
    max_profit = 0

    for r in range(1, len(honey) + 1):
        for comb in combinations(honey, r):
            if sum(comb) <= C:
                profit = sum(x ** 2 for x in comb)
                max_profit = max(max_profit, profit)

    return max_profit

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())

    #머리가 안돌아가서 하나씩 뽑는 코드를 생각했다가, 조합기반으로 수정
    arr = [list(map(int, input().split())) for _ in range(N)]

    profits = []

    for i in range(N):
        for j in range(N - M + 1):
            honey = arr[i][j:j+M]
            result = get_profit(honey, C)
            profits.append((i, j, result))

    answer = 0

    for a in range(len(profits)):
        i1, j1, profit1 = profits[a]

        for b in range(a + 1, len(profits)):
            i2, j2, profit2 = profits[b]

            # 열이 다르면 바로 더하기
            if i1 != i2:
                answer = max(answer, profit1 + profit2)
            # 열이 같다면 행이 다른지 검사하고 더하기기
            else:
                if j1 + M <= j2 or j2 + M <= j1:
                    answer = max(answer, profit1 + profit2)

    print(f"#{tc} {answer}")