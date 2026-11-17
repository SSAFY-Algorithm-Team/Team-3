# 코드트리 2-4-1-02. Date to Date (Medium)
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-date-to-date/description

# [시뮬레이션] 시작 날짜에서 하루씩 이동하며 목표 날짜까지 반복
# 월별 일수를 리스트에 저장하고, 월을 인덱스로 사용
# num_of_days[1]이 1월이 되도록 맨 앞에 0 추가

# [월 변경 조건] 날짜를 하루 늘린 뒤, 그달의 마지막 날을 넘으면 다음 달 1일로 변경
# == 사용 시 마지막 날을 건너뛰므로 > 사용

m1, d1, m2, d2 = map(int, input().split())
elapsed_days = 0

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if m1 == m2 and d1 == d2:
        elapsed_days += 1
        break
    
    elapsed_days += 1
    d1 += 1

    if d1 > num_of_days[m1]:
        m1 += 1
        d1 = 1

print(elapsed_days)
