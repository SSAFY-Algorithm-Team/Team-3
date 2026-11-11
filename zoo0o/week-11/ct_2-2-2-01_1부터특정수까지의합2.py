# 코드트리 2-2-2-01. 1부터특정수까지의합2

N = int(input())

def fact(n):
    if n == 1:
        return 1
    return fact(n-1) + n

print(fact(N))
