# 코드트리 2-4-2-01. 2진수로 변환하기 (Easy)
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-convert-to-binary/description

# [10진수 → 2진수] 수를 2로 나눈 나머지를 저장하고, 몫으로 계속 나누기
# n % 2: 2로 나눈 나머지인 0 또는 1
# n //= 2: 2로 나눈 몫으로 n 갱신
# n < 2가 되면 마지막 값인 0 또는 1을 저장하고 반복 종료
# 입력이 0이어도 0이 저장되므로 별도 처리 없이 출력 가능

# [나머지 저장 순서] 낮은 자릿수부터 저장되므로 역순으로 출력
# 예: 6 → 나머지 [0, 1, 1] → 2진수 110

# [* 언패킹] 리스트의 원소를 풀어서 각각의 값으로 전달
# digits = [1, 1, 0]일 때
# print(digits) → [1, 1, 0]
# print(*digits) → 1 1 0

# [역순 슬라이싱] 리스트[시작:끝:간격] 형식
# 시작과 끝을 생략하고 간격을 -1로 지정하면 뒤에서부터 가져오기
# digits[::-1] → [0, 1, 1]
# 원본 리스트는 그대로 유지

# [출력 구분자] sep는 separator(구분자)의 약자
# 출력할 값 사이에 넣을 문자 지정, 기본값은 공백
# sep="" 지정 시 값 사이에 공백 없이 출력

# [함께 사용] 역순으로 가져오기 → 원소 풀기 → 공백 없이 출력
# print(*digits[::-1], sep="") → 011

n = int(input())
digits = []

while True:
    if n < 2:
        digits. append(n)
        break

    digits.append(n%2)
    n //= 2

print(*digits[::-1], sep="")
