# 가위바위보 전파
# 소요시간 : 20분

# points[i] : i+1번 노드가 가리키는 노드 번호
# arr[i] : i+1번 노드의 속성
points = [2, 1, 4, 3]
arr = [2, 1, 3, 1]
T = 1
result = [2, 2, 1, 1]


def solution(points, arr, T):
    arr = arr[:]

    # T번 반복
    for _ in range(T):
        next_arr = arr[:]

        for i, target in enumerate(points):
            j = target - 1  # 노드 번호를 배열 인덱스로 변환

            # i번 인덱스의 노드가 j번 인덱스의 노드를 이기면 전파
            if arr[i] == arr[j] % 3 + 1:
                next_arr[j] = arr[i]

        arr = next_arr

    return arr