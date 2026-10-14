# 프로그래머스 Lv3. N으로 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/42895?language=python3
# 소요시간: 90분 / 시도: n

# 내 풀이 : 매우 비효율적인 풀이
from itertools import product


def compute(a, op, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/' and b != 0:
        return a // b
    return None  # 0으로 나누기


def solution(N, number):
    # 음... 최솟값이 8보다 크면 -1 return...
    # 그러면 숫자가 8개면 가능한 조합이.. 
    # 각 숫자 사이에 사칙연산 4개 + 없을 경우 1개 : 5개
    # 괄호를 넣냐 안넣냐 -> 겁나많지않나? 
    # 5^7 * 괄호 = 78,125 * () : 할만할지도?

    def all_values(nums, ops):
        if len(nums) == 1:
            return {nums[0]}
        result = set()
        for m in range(len(ops)):  # ops[m]을 마지막에 계산할 연산자로 고름
            left  = all_values(nums[:m+1], ops[:m])
            right = all_values(nums[m+1:], ops[m+1:])
            for a in left:
                for b in right:
                    v = compute(a, ops[m], b)
                    if v is not None:
                        result.add(v)
        return result

    for k in range(1, 9):  # N을 k개 쓰는 경우 (작은 것부터 → 처음 찾으면 최솟값)
        # N 사이 k-1칸마다: 사칙연산 4개 + 이어붙이기('')
        for choice in product(['+', '-', '*', '/', ''], repeat=k - 1):
            # 이어붙이기 먼저 처리: 5,'',5,'+',5 → nums=[55,5], ops=['+']
            nums, ops = [N], []
            for c in choice:
                if c == '':
                    nums[-1] = nums[-1] * 10 + N
                else:
                    ops.append(c)
                    nums.append(N)
            if number in all_values(nums, ops):
                return k
    return -1


# DP 써서 
def solution(N, number):
    S = [set() for _ in range(9)]  # S[k]: N을 k개 써서 만들 수 있는 값들

    for k in range(1, 9):
        S[k].add(int(str(N) * k))  # 이어붙이기: N, NN, NNN, ...

        for i in range(1, k):      # 왼쪽 i개 + 오른쪽 k-i개
            for a in S[i]:
                for b in S[k - i]:
                    S[k].add(a + b)
                    S[k].add(a - b)
                    S[k].add(a * b)
                    if b != 0:
                        S[k].add(a // b)

        if number in S[k]:         # 작은 k부터 보니까 처음 나온 게 최솟값
            return k

    return -1