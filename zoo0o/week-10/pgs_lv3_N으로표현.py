# DP (Dynamic Programming, 동적 계획법)
# - 큰 문제를 작은 문제로 나누고, 계산한 결과를 저장해 재사용하는 알고리즘
# - 같은 계산을 반복하지 않아 효율적으로 문제를 해결할 수 있음
# - 핵심: DP 배열 정의 → 초기값 설정 → 점화식(점화 관계) → 결과 확인

def solution(N, number):
    
    # 최솟값이 8보다 크면 -1을 반환 
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        
        # N을 이어 붙인 숫자 추가
        # "555" (문자열), 555 (정수)
        dp[i].add(int(str(N)*i))
        
        # i개를 j개와 (i-j)개로 나누어 조합
        # i=4이면 (1,3), (2,2), (3,1)
        for j in range(1, i):
            
            for a in dp[j]:
                for b in dp[i-j]:
                    
                    # 두 숫자를 사칙연산해서 dp[i]에 저장
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    
                    # 0은 나눌 수 없으므로 확인
                    # int()로 소수점 이하 버림
                    if b != 0:
                        dp[i].add(int(a / b))
                        
        # N을 i번 사용해서 number를 만들 수 있다면 반환
        # 1부터 확인하므로 처음 찾은 i가 최소값
        if number in dp[i]:
            return i

    # 8번까지 사용해도 만들 수 없다면 -1
    return -1
