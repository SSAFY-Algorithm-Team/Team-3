# 프로그래머스 Lv2. 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 소요시간: 30분 / 시도: 3회

def solution(phone_book):
    book = set(phone_book)
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in book:
                return False
    return True
