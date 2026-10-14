# 프로그래머스 Lv3. 정수 삼각형
# https://github.com/SSAFY-Algorithm-Team/Team-3
# 소요시간: 분 / 시도: n

def solution(triangle):
    # r번째 줄의 c번쨰 열에 왔을 때 가장 큰 거 저장하면 될듯?
    height = len(triangle)
    current_max = [[0] * height for _ in range(height)]
    current_max[0][0] = triangle[0][0]

    # 0층은 채워져있으니 1층부터 확인
    for r in range(1, height):
        # 1층의 경우 2열까지 채워야함
        for c in range(r+1):
            if c == 0:
                current_max[r][c] = current_max[r-1][c] + triangle[r][c]
            elif c == r:
                current_max[r][c] = current_max[r-1][c-1] + triangle[r][c]
            else:
                current_max[r][c] = max((current_max[r-1][c-1]), (current_max[r-1][c])) + triangle[r][c]

    answer = 0
    for row in current_max:
        col_max = max(row)
        answer = max(answer, col_max)
    
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))