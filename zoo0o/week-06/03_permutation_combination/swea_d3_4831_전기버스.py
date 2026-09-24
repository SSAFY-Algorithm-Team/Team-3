# SWEA 4831. 전기버스
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZ9kDS86wCTHBITH&contestProbId=AWTLS24ao9ADFAVT&probBoxId=AZ9kECgawC7HBITH&type=PROBLEM&problemBoxTitle=%EC%88%9C%EC%97%B4%EA%B3%BC+%EC%A1%B0%ED%95%A9&problemBoxCnt=5

# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))

    current = 0     # 현재 버스 위치
    count = 0       # 충전 횟수

    while current + K < N:

        # 현재 위치에서 갈 수 있는 가장 먼 곳부터 확인
        for next_stop in range(current + K, current, -1):

            if next_stop in chargers:
                current = next_stop
                count += 1
                break

        # K칸 안에 충전소가 없는 경우
        else:
            count = 0
            break

    print(f'#{tc} {count}')