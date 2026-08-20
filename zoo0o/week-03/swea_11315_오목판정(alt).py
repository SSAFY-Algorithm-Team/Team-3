# 내 풀이: 가로/세로/대각선을 각각 따로 구현
# 정석 풀이: 4방향을 방향 배열로 묶어서 한 번에 처리

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]

    # 가로, 세로, ↘, ↙
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]

    result = 'NO'

    for r in range(N):
        for c in range(N):

            # 돌이 없는 칸에서는 시작할 필요 없음
            if board[r][c] != 'o':
                continue

            for d in range(4):
                count = 0

                for move in range(5):
                    nr = r + dr[d] * move
                    nc = c + dc[d] * move

                    # 범위를 벗어나거나 돌이 아니면 중단
                    if not (0 <= nr < N and 0 <= nc < N):
                        break

                    if board[nr][nc] != 'o':
                        break

                    count += 1

                if count == 5:
                    result = 'YES'
                    break

            if result == 'YES':
                break

        if result == 'YES':
            break

    print(f'#{tc} {result}')