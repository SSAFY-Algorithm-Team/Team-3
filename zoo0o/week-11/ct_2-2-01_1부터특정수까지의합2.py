# 코드트리 / 2단계 / 2장 / 2절: 값을 반환하는 재귀함수 / 연습 1

N = int(input())

def fact(n):
    if n == 1:
        return 1
    return fact(n-1) + n

print(fact(N))
