# 프로그래머스 Lv3. 아이템줍기
# https://school.programmers.co.kr/learn/courses/30/lessons/84021
# 소요시간 : 180분 / 시도횟수 : 3회

from collections import deque

# table이 주어지면, block들의 정보를 반환하는 함수
def get_block(table):
    table_size = len(table)
    visited = [[False] * table_size for _ in range(table_size)]
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    blocks = []
    block_count = 0

    for row in range(table_size):
        for col in range(table_size):
            # table에서 0이면 볼 것도 없이 Pass
            if table[row][col] == 0:
                continue
            # 이미 방문했으면 Pass
            if visited[row][col]:
                continue
            visited[row][col] = True
            # 처음 가는 곳이면 block의 시작이라 두고, 이어진 걸 한 블록으로 처리
            block = deque([[row, col]])
            blocks.append([[row, col]])
            block_count += 1
            while block:
                r, c = block.popleft()
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    # 범위 안에 있고, 1이면 block에 추가
                    if 0 <= nr < table_size and 0 <= nc < table_size and table[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        block.append([nr, nc])
                        # 첫 번째 블록의 1 좌표들을 blocks[0]에 넣기
                        blocks[block_count - 1].append([nr, nc])

    return blocks

# get_block 함수랑 다 똑같은데, 빈칸을 찾아야되니까 game_board에서 0인 부분 찾기
def get_blank(game_board):
    table_size = len(game_board)
    visited = [[False] * table_size for _ in range(table_size)]
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    blanks = []
    blank_count = 0

    for row in range(table_size):
        for col in range(table_size):
            # table에서 1이면 볼 것도 없이 Pass
            if game_board[row][col] == 1:
                continue
            # 이미 방문했으면 Pass
            if visited[row][col]:
                continue
            visited[row][col] = True
            # 처음 가는 곳이면 block의 시작이라 두고, 이어진 걸 한 블록으로 처리
            blank = deque([[row, col]])
            blanks.append([[row, col]])
            blank_count += 1
            while blank:
                r, c = blank.popleft()
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    # 범위 안에 있고, 1이면 block에 추가
                    if 0 <= nr < table_size and 0 <= nc < table_size and game_board[nr][nc] == 0 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        blank.append([nr, nc])
                        # 첫 번째 블록의 1 좌표들을 blocks[0]에 넣기
                        blanks[blank_count - 1].append([nr, nc])

    return blanks

# blocks 정보가 주어지면, block 모양을 반환하는 함수
def block_shape(blocks):
    # 나중에 비교를 용이하게 하기 위해 최대한 좌측 상단으로 붙이자
    for i in range(len(blocks)):
        block = blocks[i]
        min_block_r, min_block_c = 51, 51
        # row, col 방향으로 얼마만큼 땡길지 찾기
        for j in range(len(block)):
            min_block_r = min(min_block_r, block[j][0])
            min_block_c = min(min_block_c, block[j][1])

        # 찾은 크기만큼 땡겨주기
        for k in range(len(block)):
            block[k][0] -= min_block_r
            block[k][1] -= min_block_c

        blocks[i] = block
    return blocks

# 두 block의 모양이 같은지 회전해가며 비교하는 함수(같으면 True, 다르면 False 반환)
def rotate_compare(block1, block2):
    if len(block1) != len(block2):
        return False

    # 회전하기 위해 N * M 배열로 변환
    block1_r, block1_c, block2_r, block2_c = 0, 0, 0, 0
    for (cord1, cord2) in zip(block1, block2):
        block1_r = max(block1_r, cord1[0])
        block1_c = max(block1_c, cord1[1])
        block2_r = max(block2_r, cord2[0])
        block2_c = max(block2_c, cord2[1])
    block1_arr = [[0] * (block1_c+1) for _ in range(block1_r+1)]
    block2_arr = [[0] * (block2_c+1) for _ in range(block2_r+1)]

    for (cord1, cord2) in zip(block1, block2):
        block1_arr[cord1[0]][cord1[1]] = 1
        block2_arr[cord2[0]][cord2[1]] = 1

    # 0, 90, 180, 270회전했을때 같은지 확인
    if block1_arr == block2_arr:
        return True
    # 시계 방향 90도 회전
    elif block1_arr == list(map(list, zip(*block2_arr[::-1]))):
        return True
    # 180도 회전
    elif block1_arr == [row[::-1] for row in block2_arr[::-1]]:
        return True
    # 270도 회전
    elif block1_arr == list(map(list, zip(*block2_arr)))[::-1]:
        return True
    # 이 중 아무것과도 일치하지 않으면
    else:
        return False

def solution(game_board, table):
    answer = 0
    blanks = block_shape(get_blank(game_board))
    blocks = block_shape(get_block(table))
    block_n = len(blocks)
    used = [False] * block_n
    for blank in blanks:
        for i in range(block_n):
            block = blocks[i]
            if rotate_compare(blank, block) and not used[i]:
                answer += len(block)
                used[i] = True
                break
    return answer

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
print(solution(game_board, table))