def solution(transactions):
    answer = 0
    
    for a, b, c, d in transactions:
        if a == b and c == d:
                answer += 1
                
    return answer