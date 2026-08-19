from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    
    prime_set = set()
    for length in range(1, len(numbers)+1):
        for p in permutations(numbers, length):
            num = int("".join(p))
            prime_set.add(num)
    
    for n in prime_set:
        if is_prime(n):
            answer += 1
    return answer