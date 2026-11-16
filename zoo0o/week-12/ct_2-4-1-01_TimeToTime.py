# 코드트리 2-4-1-01. Time to Time
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-time-to-time/description

# [시뮬레이션] 현재 상태를 일정한 단위로 바꾸며 목표 상태까지 반복
# 현재 시각이 목표 시각이면 반복 종료
# 1분씩 증가시키고, 60분이 되면 시를 1 늘리고 분을 0으로 초기화
# 반복마다 경과 시간을 1씩 누적

a, b, c, d = map(int, input().split())
elapsed_time = 0

while True:
    if a == c and b == d:
        break

    elapsed_time += 1
    b += 1

    if b == 60:
        a += 1
        b = 0

print(elapsed_time)
