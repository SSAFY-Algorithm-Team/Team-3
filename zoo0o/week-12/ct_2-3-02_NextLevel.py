# 코드트리 2-3-02. Next Level
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-next-level/description

# [튜플과 재대입]
# immutable(이뮤터블): 만든 뒤 내부 값을 바꿀 수 없다는 뜻.
# student1[2] = 90은 기존 튜플의 원소 수정이므로 불가능.
# student1 = (0, 0, 90)은 새 튜플을 만들어 다시 대입하므로 가능.

# [*를 이용한 출력]
# print(*user)는 리스트나 튜플의 원소를 풀어 전달함.
# 원소 사이의 공백은 print()가 기본으로 넣어줌.
# 지금 만든 User 객체는 원소를 하나씩 꺼내는 기능이 없어 * 사용 불가.
# 객체는 print(user.id, user.level)처럼 속성을 직접 꺼내 출력함.

user2_id, user2_level = input().split()
user2_level = int(user2_level)


class User:
    def __init__(self, id='codetree', level=10):
        self.id = id
        self.level = level


user1 = User()
print(f'user {user1.id} lv {user1.level}')
user2 = User(user2_id, user2_level)
print(f'user {user2.id} lv {user2.level}')
