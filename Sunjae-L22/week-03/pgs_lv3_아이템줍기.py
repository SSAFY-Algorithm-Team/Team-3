# 프로그래머스 Lv3. 아이템줍기
# https://school.programmers.co.kr/learn/courses/30/lessons/87694
# 소요시간: 100분 / 시도: 2회

# rectangle 정보가 주어졌을 때, 좌표에 직사각형을 그리는 함수
def make_map(rectangles):
    # return할 map의 크기를 먼저 구하자
    max_row, max_col = 0, 0

    # 우상단이 항상 좌하단보다 값이 크니까 2, 3 인덱스만 비교해주면 됨
    for rectangle in rectangles:
        max_row = max(max_row, rectangle[2])
        max_col = max(max_col, rectangle[3])

    # return해줄 map. 직사각형 범위를 1로 채운다.
    # 편의상 좌표 0인 부분은 padding할거라 +1씩 해줌
    cordinate_map = [[0] * (max_col+1) for _ in range(max_row+1)]

    for rectangle in rectangles:
        # 좌상단부터 우하단까지 1로 채운다
        for row in range(rectangle[0], rectangle[2] + 1):
            for col in range(rectangle[1], rectangle[3] + 1):
                cordinate_map[row][col] = 1

    return cordinate_map


# cordinate_map을 받아서 제일 바깥 길을 찾는 함수
def make_road(cordinate_map):
    row_size, col_size = len(cordinate_map), len(cordinate_map[0])
    road = []

    # 좌상단을 길의 시작으로 둡시다
    def find_start(cordinate_map, row_size, col_size):
        for row in range(row_size):
            for col in range(col_size):
                if cordinate_map[row][col] == 1:
                    # 처음 이동은 무조건 오른쪽. 
                    road.append((row, col))
                    road.append((row, col+1))
                    return

    find_start(cordinate_map, row_size, col_size)
                
    # 좌상단이 시작이면 오론쪽/아래로 시작인데 시계방향으로 돌자
    # visited를 만들고 테두리 도는 알고리즘 생각
    # 직전에 왼쪽(l)에서 왔다면 우선순위 : 위 -> 오른쪽 -> 아래
    # 직전에 위(u)에서 왔다면 우선순위 : 오른쪽 -> 아래 -> 왼쪽
    # 직전에 아래(d)에서 왔다면 우선순위 : 왼쪽 -> 위 -> 오른쪽
    # 직전에 오른쪽(r)에서 왔다면 우선순위 : 아래 -> 왼쪽 -> 위
    last = 'l'
    r, c = road[-1]
    while True:
        if last == 'l':
            if 0 <= r-1 < row_size and 0 <= c < col_size and cordinate_map[r-1][c] == 1:
                road.append((r-1, c))
                r -= 1
                last = 'd'
                continue
            if 0 <= r < row_size and 0 <= c+1 < col_size and cordinate_map[r][c+1] == 1:
                road.append((r, c+1))
                c += 1
                last = 'l'
                continue
            if 0 <= r+1 < row_size and 0 <= c < col_size and cordinate_map[r+1][c] == 1:
                road.append((r+1, c))
                r += 1
                last = 'u'
                continue
        elif last == 'u':
            if 0 <= r < row_size and 0 <= c+1 < col_size and cordinate_map[r][c+1] == 1:
                road.append((r, c+1))
                c += 1
                last = 'l'
                continue
            if 0 <= r+1 < row_size and 0 <= c < col_size and cordinate_map[r+1][c] == 1:
                road.append((r+1, c))
                r += 1
                last = 'u'
                continue
            if 0 <= r < row_size and 0 <= c-1 < col_size and cordinate_map[r][c-1] == 1:
                road.append((r, c-1))
                c -= 1
                last = 'r'
                continue
        elif last == 'd':
            if (r, c) == road[0]:
                break
            if 0 <= r < row_size and 0 <= c-1 < col_size and cordinate_map[r][c-1] == 1:
                road.append((r, c-1))
                c -= 1
                last = 'r'
                continue
            if 0 <= r-1 < row_size and 0 <= c < col_size and cordinate_map[r-1][c] == 1:
                road.append((r-1, c))
                r -= 1
                last = 'd'
                continue
            if 0 <= r < row_size and 0 <= c+1 < col_size and cordinate_map[r][c+1] == 1:
                road.append((r, c+1))
                c += 1
                last = 'l'
                continue
        elif last == 'r':
            if 0 <= r+1 < row_size and 0 <= c < col_size and cordinate_map[r+1][c] == 1:
                road.append((r+1, c))
                r += 1
                last = 'u'
                continue
            if 0 <= r < row_size and 0 <= c-1 < col_size and cordinate_map[r][c-1] == 1:
                road.append((r, c-1))
                c -= 1
                last = 'r'
                continue
            if 0 <= r-1 < row_size and 0 <= c < col_size and cordinate_map[r-1][c] == 1:
                road.append((r-1, c))
                r -= 1
                last = 'd'
                continue

    # 맨 뒤는 처음이랑 겹치게 되니까 빼고 return
    return road[:-1]


def solution(rectangle, characterX, characterY, itemX, itemY):
    rectangle = [[v * 2 for v in rect] for rect in rectangle]   # 지형 2배 -> 그대로 하면 그 상자끼리 딱 붙은 부분 표현이 안됨
    char = (characterX * 2, characterY * 2)                     # 두 점도 2배
    item = (itemX * 2, itemY * 2)

    road = make_road(make_map(rectangle))
    char_loc = road.index(char)
    item_loc = road.index(item)

    diff = abs(char_loc - item_loc)
    return min(diff, len(road) - diff) // 2      

rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
answer = solution(rectangle, 1, 3, 7, 8)
print(answer)