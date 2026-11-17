# 코드트리 2-3-3-04. 줄 세우기
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-line-up-students/description

# [튜플에 학생 번호 붙이기]
# 튜플끼리 + 하면 원소가 이어진 새 튜플이 만들어진다.
# 예: (170, 60) + (1,) → (170, 60, 1)
# 입력받은 (키, 몸무게)에 (i + 1,)을 붙여 학생 번호도 함께 저장한다.
# i는 0부터 시작하므로 실제 학생 번호는 i + 1이다.
# (1)은 숫자이고, (1,)은 원소 하나짜리 튜플이다. 쉼표가 필요하다.
# 번호를 함께 저장하면 정렬 후에도 원래 몇 번째 학생인지 알 수 있다.

# [정렬 기준]
# 키 내림차순 → 몸무게 내림차순 → 번호 오름차순으로 비교한다.
# 앞의 기준이 같을 때만 다음 기준을 비교한다.
# 시간복잡도: O(N log N)

n = int(input())
students = [
    tuple(map(int, input().split())) + (i + 1,)
    for i in range(n)
]

students.sort(key=lambda x: (-x[0], -x[1], x[2]))

for h, w, i in students:
    print(h, w, i)
