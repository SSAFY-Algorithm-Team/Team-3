def isPossible(arr, row, col, dir_vector):
    count = 0
    for dr in dir_vector[0]:
        for dc in dir_vector[1]:
            nr, nc = row + dr, col + dc
            if dr == 0 and dc == 0:
                continue
            if 0 <= nr < len(arr) and 0 <= nc < len(arr[0]):
                if arr[nr][nc] < arr[row][col]:
                    count += 1
    return count

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    total = 0

    height_arr = [list(map(int, input().split())) for _ in range(N)]
    dir_vector = [[-1, 0, 1], [-1, 0, 1]]

    for row, arr in enumerate(height_arr):
        for col in range(len(arr)):
            count = isPossible(height_arr, row, col, dir_vector)
            if count >= 4:
                total += 1

    print(f'#{test_case} {total}')
