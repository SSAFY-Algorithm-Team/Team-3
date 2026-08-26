# 프로그래머스 Lv3. 단어 변환
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False] * len(words)
    queue = deque([(begin,0)])

    while queue:
        curr_word, cnt = queue.popleft()
        if curr_word == target:
            return cnt

        for i in range(len(words)):
            if visited[i]:
                continue
            diff_cnt = 0
            for char1, char2 in zip(curr_word, words[i]):
                if char1 != char2:
                    diff_cnt += 1
            if diff_cnt == 1:
                visited[i] = True
                queue.append((words[i],cnt+1))
        
    return 0

solution("hit","cog", ["hot", "dot", "dog", "lot", "log", "cog"])