# 프로그래머스 Lv3. 단어 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 소요시간: 60분 / 시도: 1회

from collections import deque

def is_connected(word_a, word_b):
    diff_count = 0
    for char_a, char_b in zip(word_a, word_b):
        if char_a != char_b:
            diff_count += 1
    return diff_count == 1


def solution(begin, target, words):
    visited = [False] * len(words)
    queue = deque([(begin, 0)])

    while queue:
        cur_word, step = queue.popleft()
        
        if cur_word == target:
            return step
        
        for index in range(len(words)):
            if not visited[index] and is_connected(cur_word, words[index]):
                visited[index] = True
                queue.append((words[index], step + 1))
    
    return 0
