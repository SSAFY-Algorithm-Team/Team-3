# SWEA 14555. 공과 잡초
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYGtoa3qARcDFARC
# 소요시간: 15분 / 시도: 2회

# | 잔디 () 공
# () 1 (| 1 |) 1 이렇게만 카운트 하면 되는 거 아닌가?

T = int(input())
for tc in range(1, T + 1):
    S = input()
    count = 0

    for i in range(len(S)):
        if S[i : i + 2] == "()" or S[i : i + 2] == "(|" or S[i : i + 2] == "|)":
            count += 1

    print(f"#{tc} {count}")
