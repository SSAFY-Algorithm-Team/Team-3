# 프로그래머스 Lv2. 전화번호목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 소요시간: 5분 / 시도: 1회

phone_book = ["12","123","1235","567","88"]

# 처음 생각한 풀이
def solution1(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True


def solution2(phone_book):
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False

    root = TrieNode()

    for phone in phone_book:
        node = root

        for ch in phone:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

            # 이미 끝난 번호가 현재 경로의 일부인 경우
            if node.is_end:
                return False

        # 현재 번호가 다른 번호의 접두어인 경우
        # 예: 이미 '119'가 들어있고 지금 '1195'를 넣는 상황
        if node.children:
            return False

        node.is_end = True

    return True