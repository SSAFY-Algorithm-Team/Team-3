# 프로그래머스 Lv2. 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 소요시간: 6O분 / 시도: 2회

from itertools import permutations

def isPrime(value):
    count = 0
    for i in range(1, value + 1):
        if value % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False

def solution(numbers):
    num_arr = list(map(str, numbers))
    answer = []
    for i in range(1, len(num_arr) + 1):
        total = set(list(permutations(num_arr, i)))
        for arr in total:
            num = int("".join(arr))
            if isPrime(num) and num not in answer:
                answer.append(num)
    return len(answer)
