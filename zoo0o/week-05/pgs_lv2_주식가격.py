# 프로그래머스 Lv2. 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42628
#  소요시간: 20분 / 시도: 2회

def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
        answer.append(count)
    return answer