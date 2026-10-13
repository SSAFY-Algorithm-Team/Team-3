# 프로그래머스 Lv3. N으로 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/42895
# 소요시간: 45분 / 시도: 3회

"""
1. 처음 들었던 생각
- dp라는 배열을 만들고 1~number의 index 위치에 N으로 해당 수를 만들 수 있는 최소 횟수를 저장하면 되지 않을까?
- 근데 이러면 아래의 상황처럼 55, 60이라는 숫자가 필요함
    12 = (55 + 5) / 5
    12 = 60 / 5
=> 이 접근 법은 아니다..

2. N의 사용 횟수가 최대 8번이라는 점을 활용
dp[index] = N을 정확히 index번 사용해서 만들 수 있는 모든 숫자의 집합으로 정의해서 풀어야 겠다
"""


def solution(N, number):
    # N을 1번 ~ 8번 사용 가능
    # 중복을 피하기 위해 set 사용
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        # N을 i번 이어 붙인 숫자
        dp[i].add(int(str(N) * i))
        
        # N 사용 횟수를 2개의 그룹으로 나눔
        # 사칙연산을 적용할 두 숫자를 만들기 위해
        for j in range (1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    
                    if b != 0:
                        # 나눗셈은 0 방향으로 버림
                        q = abs(a) // abs(b)
                        if (a < 0) != (b < 0):
                            q = -q
                        dp[i].add(q)
        
        # 처음으로 number를 만들었다면
        # 이때의 i가 최소 사용 횟수
        if number in dp[i]:
            return i
        
    return -1
