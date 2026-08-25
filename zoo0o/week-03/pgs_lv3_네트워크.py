# 프로그래머스 Lv3. 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3
# 구현 > AI


def solution(n, computers):
    answer = 0
    visited = [0] * n

    def dfs(current):
        visited[current] = 1

        for i in range(n):
            if computers[current][i] == 1 and visited[i] == 0:
                dfs(i)

    for i in range(n):
        if visited[i] == 0:
            answer += 1
            dfs(i)

    return answer
