# 프로그래머스 Lv2. 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# Unsolved


def solution(numbers, target):
    answer = 0

    def dfs(idx, current_sum):
        # 1. 모든 숫자를 사용한 경우
        if idx == len(numbers):
            if current_sum == target:
                return 1
            return 0

        # 2. 남은 숫자로 target에 도달할 수 없는 경우 (가지치기)
        remain_sum = sum(numbers[idx:])
        if abs(target - current_sum) > remain_sum:
            return 0

        # 3. + / - 두 경우 탐색
        return dfs(idx + 1, current_sum + numbers[idx]) + dfs(
            idx + 1, current_sum - numbers[idx]
        )

    answer = dfs(0, 0)

    return answer
