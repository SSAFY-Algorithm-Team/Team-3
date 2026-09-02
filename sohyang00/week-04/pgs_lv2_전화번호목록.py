# 프로그래머스 Lv2. 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577


def solution(phone_book):
    phone_set = set(phone_book)
    num_book = {}

    for number in phone_book:
        for end in range(1, len(number)):
            prefix = number[:end]

            if prefix in phone_set:
                return False

    return True
