# 코드트리 / 2단계 / 2장 / 2절: 값을 반환하는 재귀함수 / 연습 2

N = int(input())

def f(n):
    if n < 10:
        return n ** 2

    return (n % 10) ** 2 + f(n // 10)

print(f(N))
