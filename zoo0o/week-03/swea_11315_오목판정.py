# SWEA 11315. 오목 판정
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXaSUPYqPYMDFASQ&
# 소요시간: 50분 / 시도: 5회

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 'NO'
    # 가로, 세로, 대각선 순서대로 확인
    for i in range(N):
        for j in range(N - 4):
            row_count = 0 
            col_count = 0 
            
            # 가로
            if arr[i][j] == 'o':
                for n in range(j, j+5):
                    if arr[i][n] == 'o':
                        row_count += 1
                    else:
                        break

            # 세로
            if arr[j][i] == 'o':
                for n in range(j, j + 5):
                    if arr[n][i] == 'o':
                        col_count += 1
                    else:
                        break

            if row_count == 5 or col_count == 5:
                result = 'YES'
                break

    # 대각선
    for i in range(N - 4):
        for j in range(N - 4):
            cross_count = 0 
            if arr[i][j] == 'o':
                for n in range(5):
                    if arr[i+n][j+n] == 'o':
                        cross_count += 1
                    else:
                        break
            if cross_count == 5:
                result = 'YES'
                break

    # 반대 대각선
    for i in range(N - 4):
        for j in range(4, N):
            cross_rvs_count = 0

            if arr[i][j] == 'o':
                for n in range(5):
                    if arr[i+n][j-n] == 'o':
                        cross_rvs_count += 1
                    else:
                        break
            if cross_rvs_count == 5:
                result = 'YES'
                break

    print(f'#{tc} {result}')