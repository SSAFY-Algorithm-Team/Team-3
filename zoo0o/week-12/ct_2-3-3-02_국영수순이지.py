# 코드트리 2-3-3-02. 국영수 순이지
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-korean-english-math-order/description

# [lambda로 여러 정렬 기준 설정]
# key=lambda x: (-x[1], -x[2], -x[3])에서 x는 학생 한 명의 튜플이다.
# x[0]은 이름, x[1]은 국어, x[2]는 영어, x[3]은 수학 점수다.
# lambda가 반환한 튜플을 왼쪽부터 비교하므로 국어, 영어, 수학 순으로 우선한다.
# 국어가 다르면 국어만 비교하고, 국어가 같을 때만 영어를 비교한다.
# 국어와 영어가 모두 같을 때만 수학을 비교한다. 세 과목의 합으로 비교하지 않는다.
# sort는 기본적으로 오름차순이므로 점수 앞에 -를 붙여 높은 점수가 먼저 오게 한다.
# 예: 80점은 -80, 70점은 -70이 되어 -80이 먼저 온다.
# 예: lee(80, 70, 50), park(80, 70, 60)은 국어와 영어가 같아 수학으로 결정한다.
# park의 -60이 lee의 -50보다 작으므로 park가 먼저 온다.
# 기준은 점수지만 실제로 순서가 바뀌는 것은 이름을 포함한 학생 튜플 전체다.
# 시간복잡도: O(N log N)

n = int(input())
students = []

for _ in range(n):
    name, korean, english, math = input().split()
    students.append((name, int(korean), int(english), int(math)))

students.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for name, korean, english, math in students:
    print(name, korean, english, math)
