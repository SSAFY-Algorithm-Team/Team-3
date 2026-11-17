# 코드트리 2-2-2-03. 1이되는순간까지

N = int(input())

def f(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return f(n//2) + 1
    else:
        return f(n//3) + 1


print(f(N))
