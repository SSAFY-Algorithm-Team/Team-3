# 프로그래머스 Lv3. 단어변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 소요시간: 45분 / 시도: 3회


from collections import deque

# 단어 두개가 주어졌을 때, 한자리만 다른지 확인하는 함수
# 한자리만 다르면 연결되어 있다고 생각하자
def connectable(word1, word2):
    diff = 0
    # 두 단어는 무조건 길이가 같음
    word_len = len(word1)
    for i in range(word_len):
        if word1[i] != word2[i]:
            diff += 1
        if diff > 1:
            return False
    if diff == 1:
        return True


def solution(begin, target, words):
    target_id = 0
    if target not in words:
        return 0
    words = [begin] + words
    target_id = words.index(target)
    n = len(words)

    # 연결가능여부를 저장해놓는 그래프 
    graph = [[False] * n for _ in range(n)]
    # 단어끼리 이어지는지
    for i in range(n):
        for j in range(i+1, n):
            if connectable(words[i], words[j]):
                graph[i][j] = True
                graph[j][i] = True

    # bfs
    visited = [False] * n
    visited[0] = True
    # 번호, 거리
    q = deque([(0, 0)])

    while q:
        row, convert = q.popleft()
        if row == target_id:
            return convert
        for col in range(n):
            if graph[row][col] and not visited[col]:
                visited[col] = True
                q.append((col, convert+1))

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))