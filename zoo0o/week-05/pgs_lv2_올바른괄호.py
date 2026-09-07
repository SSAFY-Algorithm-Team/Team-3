# 프로그래머스 Lv2. 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 소요시간: 20분 / 시도: 2회

def solution(s):
    # 닫히지 않은 '(' 개수
    count = 0

    for S in s:
        # '(' 괄호 열기
        if S == '(' and count >= 0:
            count += 1
        # ')' 괄호 닫기
        elif S == ')' and count > 0:
            count -= 1
        # 닫을 '('가 없는데 ')'가 나오면 False 반환
        else:
            return False

    # 괄호가 전부 잘 닫혔는지 확인
    if count == 0:
        return True
    else:
        return False