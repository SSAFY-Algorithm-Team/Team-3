# 복기 1. 가위바위보 전파
# 소요시간: 분 / 시도: 회

def solution(points, arr, T):
    # 인덱스 별로 가위(1), 바위(2), 보(3) 순서로 이기는 번호 저장
    # 앞에 0은 무시
    winner_list = [0, 2, 3, 1]

    for _ in range(T):
        new_arr = arr[:]
        for i in range(len(points)):
            target = points[i] - 1
            if arr[i] == winner_list[arr[target]]:
                new_arr[target] = arr[i]
        arr = new_arr

    return arr


if __name__ == "__main__":
    print(solution([2, 1, 4, 3], [2, 1, 3, 1], 1))  # [2, 2, 1, 1]
    print(solution([2, 3, 1], [2, 1, 3], 3))  # [2, 1, 3]
