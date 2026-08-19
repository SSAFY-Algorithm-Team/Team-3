# 프로그래머스 Lv2. 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839

# 숫자 조각을 1개부터 전부 사용할 때까지 순열로 배치한다.
# 같은 숫자와 앞자리 0 때문에 생기는 중복은 정수로 변환한 뒤 set으로 제거한다.

from itertools import permutations


def is_prime(number):
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def solution(numbers):
    candidates = set()

    for length in range(1, len(numbers) + 1):
        for arranged in permutations(numbers, length):
            candidates.add(int(''.join(arranged)))

    return sum(is_prime(number) for number in candidates)
