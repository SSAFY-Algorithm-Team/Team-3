import copy


# 1. 벽돌 연쇄 폭발 (DFS)
def explode(x, y, board, H, W):
    power = board[x][y]
    board[x][y] = 0  # 현재 위치 벽돌 깨뜨림

    # 벽돌 숫자가 1이면 자기 자신만 터지고 종료
    if power == 1:
        return

    # 4방향 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 적힌 숫자(power) 만큼 상하좌우 퍼져나감
    for i in range(4):
        for p in range(1, power):
            nx = x + dx[i] * p
            ny = y + dy[i] * p

            # 맵 범위 안이고 벽돌이 존재하는 경우
            if 0 <= nx < H and 0 <= ny < W:
                if board[nx][ny] > 0:
                    # 연쇄 폭발을 위해 재귀 호출
                    explode(nx, ny, board, H, W)


# 2. 스택을 이용한 중력 처리 (열 단위)
def apply_gravity(board, H, W):
    for c in range(W):  # 세로(열) 단위로 검사
        stack = []

        # 맨 아래 행(H-1)부터 위로 올라가며 0이 아닌 벽돌 수집
        for r in range(H - 1, -1, -1):
            if board[r][c] > 0:
                stack.append(board[r][c])
                board[r][c] = 0  # 일단 0으로 초기화

        # 스택에서 꺼내 아래쪽부터 다시 차곡차곡 채우기
        idx = H - 1
        for val in stack:
            board[idx][c] = val
            idx -= 1


# 3. N개의 구슬을 떨어뜨리는 모든 경우의 수 탐색 (백트래킹)
def play(count, current_board, N, W, H):
    global min_bricks

    # 현재 남아있는 벽돌 개수 세기
    remaining = sum(row.count(val) for row in current_board for val in row if val > 0)

    # 1) 벽돌이 다 깨졌거나 2) 구슬 N개를 모두 쏜 경우
    if remaining == 0 or count == N:
        min_bricks = min(min_bricks, remaining)
        return

    # 가지치기: 이미 최솟값이 0이면 더 이상 탐색할 필요 없음
    if min_bricks == 0:
        return

    # 0번 열부터 W-1번 열까지 구슬을 떨어뜨려 봄
    for col in range(W):
        # 1. 제일 위에 있는 벽돌 위치 찾기
        target_r = -1
        for r in range(H):
            if current_board[r][col] > 0:
                target_r = r
                break

        # 구슬이 떨어질 위치에 벽돌이 있는 경우만 진행
        if target_r != -1:
            # 보드판 복사 (이전 상태 보존)
            next_board = copy.deepcopy(current_board)

            # 폭발 -> 중력 -> 다음 구슬 쏘기
            explode(target_r, col, next_board, H, W)
            apply_gravity(next_board, H, W)
            play(count + 1, next_board, N, W, H)


# 메인 실행 부분
T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())

    # H개의 행을 입력받음
    mat = [list(map(int, input().split())) for _ in range(H)]

    min_bricks = float('inf')

    # 구슬 0개 떨군 상태부터 탐색 시작
    play(0, mat, N, W, H)

    print(f"#{tc} {min_bricks}")