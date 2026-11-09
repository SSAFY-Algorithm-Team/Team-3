# 2단계 / 2장 / 2절: 값을 반환하는 재귀함수 / 연습 4

N = int(input())

def f(n):
    # 첫 번째와 두 번째 값은 1
    if n == 1 or n == 2:
        return 1

    # 바로 앞의 값 + 그 앞의 값
    return f(n - 1) + f(n - 2)

print(f(N))
