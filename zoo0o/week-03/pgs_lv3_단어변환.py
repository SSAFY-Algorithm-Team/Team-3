# 프로그래머스 Lv3. 단어 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 구현 > AI

from collections import deque


def solution(begin, target, words):
    # BFS 큐
    # (현재 단어, 현재까지 변환한 횟수)
    queue = deque()
    queue.append((begin, 0))

    visited = [0] * len(words)

    # 큐에 탐색할 단어가 남아 있는 동안 반복
    while queue:
        current_word, count = queue.popleft()

        # target에 도달하면 현재 변환 횟수 반환
        if current_word == target:
            return count

        # 현재 단어에서 이동할 수 있는 다음 단어 탐색
        for word_idx in range(len(words)):
            next_word = words[word_idx]

            # 이미 방문한 단어는 다시 탐색하지 않음
            if visited[word_idx] == 1:
                continue

            diff_count = 0

            # 현재 단어와 다음 단어의 다른 글자 수 확인
            for i in range(len(begin)):
                if current_word[i] != next_word[i]:
                    diff_count += 1

            # 한 글자만 다르면 변환 가능
            if diff_count == 1:
                visited[word_idx] = 1
                queue.append((next_word, count + 1))

    # target까지 변환할 수 없는 경우
    return 0
