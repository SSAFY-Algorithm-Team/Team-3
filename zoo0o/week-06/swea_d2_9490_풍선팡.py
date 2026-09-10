# SWEA 9490. 풍선팡
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZ9kDS86wCTHBITH&contestProbId=AXAerAPaVXMDFARP&probBoxId=AZ9kDS86wCXHBITH&type=USER&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+%EA%B8%B0%EB%B3%B8&problemBoxCnt=6

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    # 상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_sum = 0

    # 1. 터뜨릴 풍선 위치 선택
    for r in range(N):
        for c in range(M):

            # 2. 가운데 풍선의 꽃가루부터 포함
            current_sum = maps[r][c]
            power = maps[r][c]

            # 3. 상하좌우 탐색
            for d in range(4):
                for dist in range(1, power + 1):
                    nr = r + dr[d] * dist
                    nc = c + dc[d] * dist

                    # 범위를 벗어나면 같은 방향은 더 볼 필요 없음
                    if not (0 <= nr < N and 0 <= nc < M):
                        break

                    current_sum += maps[nr][nc]

            # 4. 최대값 갱신
            max_sum = max(max_sum, current_sum)

    print(f'#{tc} {max_sum}')