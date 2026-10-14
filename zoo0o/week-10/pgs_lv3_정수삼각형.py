
# 프로그래머스 Lv3. 정수 삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 소요시간: / 시도:

# [이 문제에서의 DP]
# - dp[i][j]: (i, j) 칸까지 도달했을 때의 최대 누적 합
# - 이전 행의 왼쪽 위와 오른쪽 위 중 더 큰 누적 합을 선택
# - 맨 왼쪽과 맨 오른쪽은 들어올 수 있는 경로가 하나뿐
# - 마지막 행의 최댓값이 정답


def solution(triangle):
    # triangle과 동일한 모양의 2차원 DP 배열 생성
    # 각 행의 길이가 달라도 2차원 리스트 생성 가능
    dp = [[0] * len(row) for row in triangle]

    # 꼭대기는 이전 경로가 없으므로 그대로 저장
    dp[0][0] = triangle[0][0]

    # 두 번째 행부터 마지막 행까지 순회
    for i in range(1, len(triangle)):
        # 현재 행에 존재하는 모든 칸 순회
        for j in range(len(triangle[i])):

            if j == 0:
                # 맨 왼쪽: 바로 위에서만 내려올 수 있음
                dp[i][j] = dp[i-1][j] + triangle[i][j]

            elif j == i:
                # 맨 오른쪽: 왼쪽 위에서만 내려올 수 있음
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]

            else:
                # 가운데: 왼쪽 위와 오른쪽 위 중 큰 누적 합 선택
                dp[i][j] = triangle[i][j] + max(
                    dp[i-1][j-1],
                    dp[i-1][j]
                )

    # 마지막 행에 저장된 누적 합 중 최댓값 반환
    return max(dp[-1])
