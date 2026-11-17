# 코드트리 2-2-2-04. 재귀함수를이용한피보나치수

N = int(input())

def f(n):
    # 첫 번째와 두 번째 값은 1
    if n == 1 or n == 2:
        return 1

    # 바로 앞의 값 + 그 앞의 값
    return f(n - 1) + f(n - 2)

print(f(N))
