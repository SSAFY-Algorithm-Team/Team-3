# 프로그래머스 Lv2. 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 소요시간: 10분 / 시도: 3회

def solution(prices):
    n = len(prices)
    answer = []
    for i in range(n):
        total = 0
        for j in range(i + 1, n):
            total += 1
            if prices[j] < prices[i]:
                break
        answer.append(total)
    return answer
