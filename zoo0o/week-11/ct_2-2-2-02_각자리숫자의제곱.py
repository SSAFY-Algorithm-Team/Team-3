# 코드트리 2-2-2-02. 각자리숫자의제곱

N = int(input())

def f(n):
    if n < 10:
        return n ** 2

    return (n % 10) ** 2 + f(n // 10)

print(f(N))
