# 프로그래머스 Lv3. N으로 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/42895
# 소요시간: __분 / 시도: __회

# dp[1] => 1개로 만들 수 있는 조합
# dp[2] => 2개로 만들 수 있는 조합

def solution(N, number):
    # d[1]: 5
    # d[2]: 55, 5-5, 5+5, 5*5, 5//5
    # d[2]: d[1]+d[1], d[1]-d[1], d[1]+d[1], d[1]*d[1], d[1]//d[1]
    # d[3]: d[1]+d[1]+d[1], d[2]-d[1], d[2]+d[1], d[2]*d[1], d[2]//d[1]
    # d[4]: d[1]..., d[3]-d[1]
    dp = [set() for _ in range(9)]
    result = -1
    dp[1].add(N)

    if number == N:
        print(1)
        return 1

    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        for j in range(1,i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a-b)
                    dp[i].add(a+b)
                    dp[i].add(a*b)
                    if b != 0:
                        dp[i].add(a//b)

        if number in dp[i]: 
            result = i
            break
    print(result)
    return result

solution(5, 12)
solution(2, 11)