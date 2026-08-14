# SWEA 12712. 파리퇴치3
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXuARWAqDkQDFARa
# 소요시간: 20분 / 시도: 1회

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    plus_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cross_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    answer = 0

    for r in range(N):
        for c in range(N):
            plus_sum = arr[r][c]
            cross_sum = arr[r][c]

            for dr, dc in plus_dirs:
                for k in range(1, M):
                    nr = r + dr * k
                    nc = c + dc * k

                    if 0 <= nr < N and 0 <= nc < N:
                        plus_sum += arr[nr][nc]

            for dr, dc in cross_dirs:
                for k in range(1, M):
                    nr = r + dr * k
                    nc = c + dc * k

                    if 0 <= nr < N and 0 <= nc < N:
                        cross_sum += arr[nr][nc]

            answer = max(answer, plus_sum, cross_sum)

    print(f"#{test_case} {answer}")
