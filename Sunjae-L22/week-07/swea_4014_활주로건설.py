# swea [모의 SW 역량테스트] 활주로건설
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZ9kDS86wCTHBITH&contestProbId=AWIeW7FakkUDFAVH&probBoxId=AZ9kECgawC7HBITH&type=PROBLEM&problemBoxTitle=%EC%88%9C%EC%97%B4%EA%B3%BC+%EC%A1%B0%ED%95%A9&problemBoxCnt=5
# 소요시간: 30분 / 시도: 1회

# 4014. 활주로 건설
# 경사로 설치 가능 조건 : 높이 차이 1, 낮은 지형의 높이 > 경사로의 길이

def can_build(row, X):
    # 현재 높이가 연속되는 수
    cont = 1
    now = row[0]

    for i in range(1, len(row)):
        if row[i] == now:
            cont += 1

        else:
            # 높이 차이가 2 이상이면 설치 불가능
            if abs(row[i] - now) > 1:
                return False

            # 오르막 : 이전의 낮은 지형이 X칸 이상 필요
            elif row[i] > now:
                if cont < X:
                    return False
                cont = 1

            # 내리막 : 현재 칸부터 낮은 지형 X칸이 필요
            else:
                # 이전 내리막 경사로가 아직 완성되지 않은 경우
                if cont < 0:
                    return False

                # 앞으로 X - 1칸 필요
                cont = 1 - X
            now = row[i]

    # 끝까지 확인했는데 내리막 경사로가 미완성이면 불가능
    return cont >= 0


T = int(input())

for test_case in range(1, T + 1):
    N, X = map(int, input().split())

    ground = []
    for i in range(N):
        ground.append(list(map(int, input().split())))

    answer = 0

    # 가로 방향 확인
    for row in ground:
        if can_build(row, X):
            answer += 1

    # 세로 방향 확인
    for col in zip(*ground):
        if can_build(col, X):
            answer += 1

    print(f"#{test_case} {answer}")