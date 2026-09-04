# 프로그래머스 Lv2. 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# AI 설계 > 사유 완전 탐색이 아닌 해시로는 어떻게 푸는 걸까...?

def solution(phone_book):
    # 전화번호 존재 여부를 빠르게 확인하기 위해 set으로 변환
    phone_set = set(phone_book)

    # 1. 전화번호를 하나씩 확인
    for number in phone_book:
        # 2. 자기 자신을 제외한 모든 접두사 생성
        for i in range(1, len(number)):
            prefix = number[:i]

            # 3. 접두사가 실제 전화번호로 존재하면 조건 위반
            if prefix in phone_set:
                return False

    # 모든 번호를 확인해도 접두사가 없으면 True
    return True