# 프로그래머스 Lv3. 퍼즐 조각 채우기
# https://school.programmers.co.kr/learn/courses/30/lessons/84021
# 소요시간: 120분 / 시도: 1회

from collections import deque, Counter

def rotate(cells):
    """도형을 시계방향 90도 회전시키고, 좌상단에 붙여 정렬한 좌표 리스트를 반환."""
    # (r, c) -> (c, -r). 열 좌표가 음수가 되면서 왼쪽으로 삐져나갈 수 있다.
    turned = [(c, -r) for r, c in cells]

    # 최소 행/열을 빼서 원점 쪽으로 당긴다.
    # 이 과정 덕분에 위에서 음수가 나와도 신경 쓸 필요가 없고,
    # 판 위 절대 위치가 사라져서 다른 도형과 비교가 가능해진다.
    min_r = min(r for r, c in turned)
    min_c = min(c for r, c in turned)

    # 정렬까지 해야 같은 모양이 항상 같은 순서로 나와 == 비교가 성립한다.
    return sorted((r - min_r, c - min_c) for r, c in turned)


def normalize(cells):
    """도형의 대표형(회전·위치와 무관한 고유 식별자)을 반환."""
    candidates = []
    shape = cells

    # 4번 돌리면 마지막에 원본으로 돌아온다.
    # 즉 원본을 따로 넣지 않아도 4가지 회전이 모두 후보에 포함되고,
    # 원본 역시 rotate를 거쳤으므로 당기기+정렬이 적용된 상태다.
    for _ in range(4):
        shape = rotate(shape)
        candidates.append(shape)

    # 4개 중 사전순 최소를 대표형으로 삼는다. 어떤 게 뽑히는지는 중요하지 않고,
    # "같은 모양이면 항상 같은 게 뽑힌다"는 점만 있으면 된다.
    # 뒤집기는 규칙상 금지이므로 회전 4가지만 본다. (거울상은 다른 대표형이 된다)
    # Counter 키로 쓰려면 해시 가능해야 하므로 tuple로 변환.
    return tuple(min(candidates))


def extract(board, target):
    """판에서 target 값으로 연결된 덩어리들을 찾아, 각각의 좌표 리스트로 반환.

    game_board는 빈칸을 찾으므로 target=0, table은 조각을 찾으므로 target=1.
    """
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    shapes = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        for j in range(n):
            # 아직 어느 덩어리에도 속하지 않은 target 칸 = 새 덩어리의 시작점
            if board[i][j] == target and not visited[i][j]:
                visited[i][j] = True
                cells = []          # 이번 덩어리의 좌표를 모을 리스트
                q = deque()
                q.append((i, j))

                while q:
                    r, c = q.popleft()
                    cells.append((r, c))    # 꺼낸 칸은 이미 검증된 칸

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if nr < 0 or nr >= n or nc < 0 or nc >= n:
                            continue

                        if visited[nr][nc] or board[nr][nc] != target:
                            continue

                        # 꺼낼 때가 아니라 넣을 때 표시해야 같은 칸이 큐에 중복으로
                        # 들어가지 않는다. 좌표를 수집하는 구조라 중복이 그대로
                        # 결과에 남아 대표형 비교가 깨진다.
                        visited[nr][nc] = True
                        q.append((nr, nc))

                shapes.append(cells)

    return shapes


def solution(game_board, table):
    # 핵심 관찰: "새로 놓은 조각과 인접한 칸이 비어있으면 안 된다"는 규칙 때문에
    # 조각은 빈칸 덩어리와 모양이 정확히 일치할 때만 놓을 수 있다.
    # 부분적으로 채우고 나머지를 다른 조각으로 메우는 경우가 없으므로,
    # 배치 탐색이 아니라 모양 매칭 문제가 된다.
    holes = Counter(normalize(s) for s in extract(game_board, 0))
    pieces = Counter(normalize(s) for s in extract(table, 1))

    # 대표형이 같으면 서로 완전히 같은 모양이라, 어떤 구멍에 먼저 쓰든 결과가 같다.
    # 따라서 그리디/이분 매칭 없이 개수만 세면 된다.
    answer = 0
    for shape, count in pieces.items():
        if shape in holes:
            # min으로 적은 쪽에 맞춘다 (조각이 남거나 구멍이 남는 경우 처리).
            # len(shape)는 그 도형의 칸 수 — 문제가 요구하는 건 조각 개수가 아니라 칸 수.
            answer += min(count, holes[shape]) * len(shape)

    # 6칸을 넘는 큰 빈칸 덩어리는 어떤 조각과도 대표형이 일치하지 않아
    # 자연스럽게 걸러진다. 별도 필터링 불필요.
    return answer
