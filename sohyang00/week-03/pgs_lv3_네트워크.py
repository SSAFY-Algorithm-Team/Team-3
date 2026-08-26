# 프로그래머스 Lv3. 네트워크
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque
def solution(n, computers):

    visited = [False] * n

    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue:
            curr = queue.popleft()
            for nv in range(n):
                if(computers[curr][nv] == 1 and not visited[nv]):
                    visited[nv] = True
                    queue.append(nv)
    answer = 0
    for computer in range(n):
        if not visited[computer]:
            answer += 1
            bfs(computer)

    return answer
