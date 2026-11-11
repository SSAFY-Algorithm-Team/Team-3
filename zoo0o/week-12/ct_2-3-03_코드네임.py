# 코드트리 2-3-03. 코드네임
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-code-name/description

# [lambda]
# lambda user: user[1]은 요원 한 명을 받아 점수(user[1])를 반환하는 짧은 함수.
# 콜론(:) 앞은 전달받을 값의 이름, 뒤는 반환할 값.
# user는 임시 이름이므로 lambda x: x[1]로 써도 같음.
# key에 넣으면 min이 각 요원의 점수를 꺼내 비교 기준으로 사용함.
# 람다 자체가 반복하는 것은 아니며, 각 요원에게 적용하는 것은 min이 함.

MAX_N = 5
users = []

for _ in range(MAX_N):
    codename, score = input().split()
    users.append((codename, int(score)))

user = min(users, key=lambda user: user[1])
print(*user)
