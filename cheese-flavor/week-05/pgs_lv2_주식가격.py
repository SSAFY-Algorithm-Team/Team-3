# 프로그래머스 Lv2. 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 소요시간: 10분 / 시도: 2회

# 큐로 다시한번 풀어보기
def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n):
        count = 0
        for j in range(i+1,n):
            count += 1
            if prices[i] > prices[j]:
                break
                
        answer.append(count)
                
    return answer


    
            
            
            
        
    


