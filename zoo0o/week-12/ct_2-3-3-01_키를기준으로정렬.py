# 코드트리 2-3-3-01. 키를 기준으로 정렬
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-sort-by-height/description

# [객체 정렬]
# 이름, 키, 몸무게를 튜플로 묶으면 정렬할 때 함께 이동한다.
# 키만 따로 정렬하면 이름과 몸무게는 그대로여서 정보가 섞인다.
# 클래스는 x.height처럼 속성으로, 튜플은 x[1]처럼 인덱스로 접근한다.
# 이 문제는 튜플로 묶으면 충분하다.
#
# [기본 코드 변경]
# 기본 입력 코드를 바꿔도 된다. 입력받을 때부터 튜플로 묶어 저장했다.
#
# [lambda와 key]
# lambda는 이름 없는 함수다. 콜론 앞은 매개변수, 뒤는 반환값이다.
# key=lambda x: x[1]에서 x는 한 사람의 튜플이다.
# x가 ('lee', 167, 40)이면 x[1]은 키인 167이다.
# 키를 비교해서 정렬하되, 실제로는 튜플 전체의 순서를 바꾼다.
# x[1]은 키 오름차순, -x[1]은 키 내림차순 정렬이다.
#
# [입력과 언패킹]
# 입력값은 문자열이므로 키와 몸무게는 int로 변환한다.
# for name, h, w in peoples는 튜플의 세 값을 각각 꺼내는 언패킹이다.
# 시간복잡도: O(N log N)

n = int(input())
peoples = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    peoples.append((n_i, int(h_i), int(w_i)))

peoples.sort(key=lambda x: x[1])

for name, h, w in peoples:
    print(name, h, w)
