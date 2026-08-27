# 프로그래머스 Lv3. 아이템 줍기
# https://school.programmers.co.kr/learn/courses/30/lessons/87694
# 설계 > AI

# rectangle [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y]
# 직사각형 개수 1~4개
# - queue니까 visited가 필요할 것
# - 이거 2차원 배열을 만들어서 직사각형이 존재하는 거 1로 채움
# - 뒤에 게임맵 최단거리랑 똑같이?? > 게임 맵 최단 거리 코드 참고
# - x,y 좌표를 변환 없이 사용하기 위해서 0~max값을 범위로

# 직사각형 내부는 0으로 두고, 테두리만 1로 만드는 방법 >> AI
# 1. 직사각형 영역 전체를 먼저 표시 > 1표시 range(x1, x2 + 1), range(y1, y2 + 1)
# 2. 직사각형 내부는 이동 불가능하게 표시 > 안쪽에 2표시 range(x1 + 1, x2), range(y1 + 1, y2)
# 3. 최종적으로 바깥 테두리만 이동 가능하게 남김

# 문제점: 점만으로 판단하니까 (2,3) (3,3) 연결X도 연결 되었다고 판단 > 2배처리를 통해서 점이 아닌 선을 표현

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    # x, y 좌표를 그대로 사용하기 위해 0 ~ max 좌표까지 생성
    max_x = max(rect[2] for rect in rectangle)
    max_y = max(rect[3] for rect in rectangle)

    maps = [[0] * (max_y + 1) for _ in range(max_x + 1)]

    # 1. 모든 직사각형 영역을 1로 채우기
    for i in range(len(rectangle)):
        x1, y1, x2, y2 = rectangle[i]

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                maps[x][y] = 1

    # 2. 각 직사각형의 내부를 2로 변경
    # 다른 직사각형의 테두리와 겹쳐도 내부라면 이동할 수 없음
    for i in range(len(rectangle)):
        x1, y1, x2, y2 = rectangle[i]

        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                maps[x][y] = 2

    # 3. BFS 준비
    visited = [[0] * (max_y + 1) for _ in range(max_x + 1)]

    queue = deque()
    queue.append((characterX, characterY, 0))
    visited[characterX][characterY] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 4. 테두리인 1만 따라 BFS
    while queue:
        x, y, count = queue.popleft()

        if x == itemX and y == itemY:
            return count

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx <= max_x and 0 <= ny <= max_y:
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, count + 1))

    return 0
