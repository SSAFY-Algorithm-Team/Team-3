# 프로그래머스 Lv3. 정수 삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 소요시간: 20분 / 시도: 2회

# 같은 위치에 도달하는 여러 경로 중, 
# 앞으로의 계산에 필요한 최댓값만 남긴다

def solution(triangle):
    dp = [[0] * len(row) for row in triangle]
    dp[0][0] = triangle[0][0]

    for row in range(1, len(triangle)):
        for col in range(len(triangle[row])):
            if col == 0:
                # 맨 왼쪽
                dp[row][col] = dp[row - 1][col] + triangle[row][col]

            elif col == row:
                # 맨 오른쪽
                dp[row][col] = dp[row - 1][col - 1] + triangle[row][col]

            else:
                # 중간
                dp[row][col] = max(
                    dp[row - 1][col - 1],
                    dp[row - 1][col]
                ) + triangle[row][col]

    return max(dp[-1])
