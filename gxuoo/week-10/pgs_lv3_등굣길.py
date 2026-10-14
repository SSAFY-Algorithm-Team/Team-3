# 프로그래머스 Lv3. 등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 소요시간: 30분 / 시도: 2회

'''
학교에서 집으로 거꾸로 DP를 하면 되지 않을까?
2차원 배열을 만들고 배열의 각 위치는 해당 위치를 지나간 길의 개수를 저장,
최종 (0, 0) 인덱스의 값을 (1, 0)값과 (0, 1)값을 더해서 최종 값을 출력해보자.
'''

def solution(m, n, puddles):
    MOD = 1_000_000_007
    field = [[0] * m for _ in range(n)]

    # 물웅덩이 위치를 -1로 변경
    for puddle in puddles:
        field[puddle[1] - 1][puddle[0] - 1] = -1

    # 학교 위치는 경로 1개로 시작
    field[n - 1][m - 1] = 1

    # 학교에서 집 방향으로 거꾸로 계산
    for row in range(n - 1, -1, -1):
        for col in range(m - 1, -1, -1):

            # 물웅덩이 또는 학교라면 건너뛰기
            if field[row][col] == -1:
                continue

            if row == n - 1 and col == m - 1:
                continue

            # 아래쪽 경로 더하기
            if row + 1 < n and field[row + 1][col] != -1:
                field[row][col] += field[row + 1][col]

            # 오른쪽 경로 더하기
            if col + 1 < m and field[row][col + 1] != -1:
                field[row][col] += field[row][col + 1]

            field[row][col] %= MOD

    return field[0][0]
