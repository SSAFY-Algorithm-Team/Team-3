# 프로그래머스 Lv3. N으로 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/42895
# 소요시간: 80분 / 시도: 4회


def solution(N, number):
    dp = [set() for _ in range(9)]

    for k in range(1, 9): #최대 9이하
        
        # 문자형태로 숫자 합친거 하나 추가
        dp[k].add(int(str(N) * k))
        
        # 숫자를 이어 붙인 경우 체크
        if number in dp[k]:
            return k
        
        for i in range(1, k):

            #양방향으로 계산(앞순서에 올수도 뒷 순서에 올수도 있으니께)
            for a in dp[i]:
                for b in dp[k-i]:
                    #사칙연산
                    dp[k].add(a+b)
                    dp[k].add(a-b)
                    dp[k].add(a*b)
                    
                    if b != 0:  #0으로 나누는거 제외
                        dp[k].add(int(a/b)) #음수일 경우 내림이 되어서 이렇게
                        #dp[k].add(int(a//b))
                    
                    # 배열 한줄 연산 끝날때마다 가지치기용 (-> 조기종료 표현을 쓰랭)
                    if number in dp[k]:
                        return k

    return -1


    
            
            
            
        
    


