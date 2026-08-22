# bfs 방식에 너무 익숙하지 않아서 ai의 도움을 받아 풀었습니다. zip함수와 enumerate 함수를 요긴하게 써야겠습니다.

from collections import deque

# 하나만 겹치는지 확인하는 함수
def one_diff(first, second):
    sum = 0
    # zip으로 묶어서 한 번에 비교
    for a, b in zip(first, second):
        if a != b:
            sum += 1
    return sum == 1

def solution(begin, target, words):
    # words에 target 단어 없으면 0을 리턴
    if target not in words:
        return 0
    # words 단어 방문했는지 확인하는 용도
    visited = [False for _ in range(len(words))]
    queue = deque([(begin, 0)])
    
    while queue:
        current_word, steps = queue.popleft()
        # 단어 같으면 횟수 반환
        if current_word == target:
            return steps
        
        for i, word in enumerate(words):
            if not visited[i] and one_diff(current_word, word):
                visited[i] = True
                queue.append((word, steps+1))
    # queue 다 돌 때까지 목표 단어 도달못하면 0 리턴
    answer = 0
    return answer