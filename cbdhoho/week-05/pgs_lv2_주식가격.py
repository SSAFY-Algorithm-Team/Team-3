def solution(prices):
    answer = []
    for idx, p in enumerate(prices):
        answer.append(0)
        for i in range(idx, len(prices)-1):
            if prices[i+1] < p:
                answer[idx] += 1
                break
            else:                 
                answer[idx] += 1
    return answer