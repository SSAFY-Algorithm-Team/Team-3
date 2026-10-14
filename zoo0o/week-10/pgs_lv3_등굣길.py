
# 프로그래머스 Lv3. 등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 소요시간: / 시도:

# [이 문제에서의 DP]
# - dp[i][j]: 집에서 (i, j) 칸까지 도달할 수 있는 경로의 개수
# - 오른쪽과 아래쪽으로만 이동 가능
# - 따라서 현재 칸 = 위쪽 경로 수 + 왼쪽 경로 수
# - 물웅덩이는 지나갈 수 없으므로 경로 수를 0으로 유지
# - 문제 좌표는 (x, y), 배열 인덱스는 [y][x] 순서
# - 경로 개수를 1,000,000,007로 나눈 나머지 반환


def solution(m, n, puddles):
    MOD = 1000000007

    # n행 m열의 2차원 DP 배열 생성
    dp = [[0] * m for _ in range(n)]

    # 물웅덩이 좌표를 배열 인덱스로 변환
    # 문제는 1부터 시작하지만 배열 인덱스는 0부터 시작
    water = {(y-1, x-1) for x, y in puddles}

    # 출발점: 집에서 출발하는 경우는 1가지
    dp[0][0] = 1

    # 모든 칸을 왼쪽 위부터 순서대로 탐색
    for i in range(n):
        for j in range(m):

            # 물웅덩이는 지나갈 수 없으므로 건너뛰기
            if (i, j) in water:
                continue

            # 출발점은 이미 1로 설정했으므로 건너뛰기
            if i == 0 and j == 0:
                continue

            # 위쪽에서 내려오는 경로
            if i > 0:
                dp[i][j] += dp[i-1][j]

            # 왼쪽에서 오는 경로
            if j > 0:
                dp[i][j] += dp[i][j-1]

            # 경로 개수가 커질 수 있으므로 나머지 연산
            dp[i][j] %= MOD

    # 오른쪽 아래 학교까지 도달하는 경로 개수
    return dp[n-1][m-1]
