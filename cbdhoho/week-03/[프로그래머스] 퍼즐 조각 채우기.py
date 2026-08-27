def get_blocks(board, target):
    """
    board(2차원 배열)에서 값이 target인 칸들을 찾아
    서로 붙어있는(상하좌우 연결) 덩어리(블록) 단위로 묶어서 반환.
    예: game_board에 대해 target=0 을 넘기면 '구멍'들의 좌표 리스트를 얻고,
        table에 대해 target=1 을 넘기면 '퍼즐 조각'들의 좌표 리스트를 얻는다.
    """
    n = len(board)
    # 이미 방문(어느 블록에 포함되었는지 처리)한 칸인지 체크하는 표
    visited = [[False]*n for _ in range(n)]
    blocks = []  # 찾아낸 블록들을 모아둘 리스트 (블록 하나 = 좌표 리스트)

    for i in range(n):
        for j in range(n):
            # target 값을 가진, 아직 방문 안 한 칸을 발견하면
            # 여기서부터 BFS 시작 -> 붙어있는 칸들을 전부 하나의 블록으로 묶는다
            if board[i][j] == target and not visited[i][j]:
                queue = [(i, j)]
                visited[i][j] = True
                block = []  # 이번에 찾을 블록에 속하는 좌표들

                while queue:
                    r, c = queue.pop()
                    block.append((r, c))
                    # 상, 하, 좌, 우 네 방향을 확인
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr, nc = r+dr, c+dc
                        # 보드 범위 안이고, 아직 방문 안 했고, target 값이면
                        # 같은 블록에 속하는 칸이므로 큐에 추가
                        if 0 <= nr < n and 0 <= nc < n \
                           and not visited[nr][nc] and board[nr][nc] == target:
                            visited[nr][nc] = True
                            queue.append((nr, nc))

                # 블록을 찾았으면, 위치에 상관없이 "모양"만 비교할 수 있도록
                # 정규화(normalize)해서 저장 (아래 normalize 함수 참고)
                blocks.append(normalize(block))
    return blocks


def normalize(block):
    """
    블록의 좌표들을 (0,0) 기준으로 평행이동시켜서 표준화.
    -> 같은 모양이라도 board 상 위치가 다르면 좌표값이 다른데,
       이걸 최솟값 기준으로 맞춰주면 "위치 무관, 모양만" 비교 가능해진다.
    예: [(3,4),(3,5),(4,4)] -> 최소 r=3, 최소 c=4를 빼면 -> [(0,0),(0,1),(1,0)]
    """
    min_r = min(r for r, c in block)
    min_c = min(c for r, c in block)
    # 정렬까지 해줘야 두 블록을 리스트끼리 '==' 비교했을 때
    # 좌표 순서가 달라서 다르다고 오판하는 걸 방지할 수 있음
    return sorted((r - min_r, c - min_c) for r, c in block)


def rotate(block):
    """
    블록을 시계 방향으로 90도 회전.
    회전 공식: (r, c) -> (c, -r)
    (좌표평면에서 시계방향 90도 회전 변환)
    회전하고 나면 좌표에 음수가 생길 수 있으므로
    다시 normalize 해서 (0,0) 기준으로 맞춰준다.
    """
    return normalize([(c, -r) for r, c in block])


def solution(game_board, table):
    # game_board에서 0인 칸들 = 채워야 할 구멍들의 모양 리스트
    holes = get_blocks(game_board, 0)
    # table에서 1인 칸들 = 끼워넣을 수 있는 퍼즐 조각들의 모양 리스트
    pieces = get_blocks(table, 1)

    # 각 piece가 이미 사용됐는지 여부 (한 조각은 한 구멍에만 쓸 수 있음)
    used = [False] * len(pieces)
    answer = 0  # 채운 칸의 총 개수 (정답)

    # 구멍 하나씩 순회하면서, 맞는 조각을 찾아본다
    for hole in holes:
        for i, piece in enumerate(pieces):
            # 이미 사용된 조각이거나, 칸 수부터 다르면 볼 필요 없이 스킵
            if used[i] or len(piece) != len(hole):
                continue

            # 이 piece를 0°, 90°, 180°, 270° 로 회전시킨 4가지 모양을 만든다
            cur = piece
            rotations = [cur]
            for _ in range(3):
                cur = rotate(cur)
                rotations.append(cur)

            # 회전된 모양들 중 하나라도 구멍 모양과 정확히 일치하면 매칭 성공
            if hole in rotations:
                used[i] = True          # 이 조각은 다 썼다고 표시
                answer += len(hole)     # 채운 칸 수만큼 answer에 더함
                break                   # 이 구멍은 처리 끝났으니 다음 구멍으로

    return answer