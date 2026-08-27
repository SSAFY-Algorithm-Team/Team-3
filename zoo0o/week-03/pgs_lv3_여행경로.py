# 프로그래머스 Lv3. 여행 경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 구현 > AI


def solution(tickets):
    tickets.sort()

    n = len(tickets)
    answer = ["ICN"]
    visited = [0] * n

    def dfs(current):
        if len(answer) == n + 1:
            return True

        for i in range(n):
            if tickets[i][0] == current and visited[i] == 0:
                visited[i] = 1
                answer.append(tickets[i][1])

                if dfs(tickets[i][1]):
                    return True

                visited[i] = 0
                answer.pop()

        return False

    dfs("ICN")
    return answer
