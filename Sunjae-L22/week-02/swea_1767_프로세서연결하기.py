# SWEA D?. 벽돌깨기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf
# 소요시간: 240분 / 시도: n회

T = int(input())


def connect_core(N, axinos, cores):
    core_n = len(cores)
    # 연결된 코어 수, 전선 길이 함(전선 길이 합은 짧을수록 굳)
    answer = [0, 0]
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]


    # 전선 연결하는 함수
    # 연결 가능하면 연결 수 길이 반환, 막히면 0
    def connect(row, col, d):
        next_row, next_col = row + dr[d], col + dc[d]
        length = 0
        # 연결 가능한지 확인
        while 0 <= next_row < N and 0 <= next_col < N:
            if axinos[next_row][next_col] != 0:
                return 0
            length += 1
            next_row += dr[d]
            next_col += dc[d]

        next_row, next_col = row + dr[d], col + dc[d]
        # 연결 가능하면 연결
        while 0 <= next_row < N and 0 <= next_col < N:
            axinos[next_row][next_col] = 2
            next_row += dr[d]
            next_col += dc[d]
        return length


    # 전선 없애는 함수
    def remove(row, col, d):
        next_row, next_col = row + dr[d], col + dc[d]
        while 0 <= next_row < N and 0 <= next_col < N:
            axinos[next_row][next_col] = 0
            next_row += dr[d]
            next_col += dc[d]


    def dfs(depth, connected, length):
        remain = core_n - depth

        # 가지치기 : 남은 코어 모두 연결해도 최고개수 못 넘을 때
        if connected + remain < answer[0]:
            return

        # 가지치기 : 남은 코어 모두 연결해도 동점인데 길이가 이미 더 긴 경우
        if connected + remain == answer[0] and length >= answer[1]:
            return

        if depth == core_n:
            # 연결된 개수가 더 많거나 개수는 같은데 길이가 더 짧으면 답 갱신
            if connected > answer[0] or (connected == answer[0] and length < answer[1]):
                answer[0], answer[1] = connected, length
            return

        row, col = cores[depth]
        # 4방향으로 연결 시도
        for d in range(4):
            wire = connect(row, col, d)            
            if wire:
                dfs(depth + 1, connected + 1, length + wire)   
                remove(row, col, d)
        # 4방향 다 연결 실패하면 depth만 +1
        dfs(depth + 1, connected, length)

    dfs(0, 0, 0)
    return answer[1]


for tc in range(1, T+1):
    N = int(input())
    axinos = [list(map(int, input().split())) for _ in range(N)]

    # 코어의 좌표 목록
    cores = []
    for row in range(N):
        for col in range(N):
            if axinos[row][col] == 1 and 0 < row < N - 1 and 0 < col < N - 1:
                cores.append((row, col))
    core_n = len(cores)

    print(f"#{tc} {connect_core(N, axinos, cores)}")