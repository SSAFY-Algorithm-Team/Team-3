# 프로그래머스 Lv2. 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for now, price in enumerate(prices):
        while stack:
            start, past_price = stack[-1]

            if past_price <= price:
                break

            stack.pop()
            answer[start] = now - start

        stack.append((now, price))

    last = len(prices) - 1
    for start, past_price in stack:
        answer[start] = last - start

    return answer

solution([1, 2, 3, 2, 3])