# 가위바위보 전파
# N <= 5000, T <= 50
# 시간복잡도: O(N * T)

def solution(points, arr, T):

    # T초 동안 반복
    for _ in range(T):
        # 이번 초의 결과를 저장할 배열
        # 동시에 변화해야 하므로 arr를 직접 수정하면 안 됨
        next_arr = arr[:]

        # i번 노드가 어디를 가리키는지 확인
        for i in range(len(points)):
            # points는 노드 번호가 1부터 시작하므로 -1
            target = points[i] - 1

            # 현재 target을 이기는 속성
            # 1(가위) -> 2(바위)
            # 2(바위) -> 3(보)
            # 3(보)   -> 1(가위)
            win = arr[target] % 3 + 1

            # i번 노드가 target을 이긴다면
            # i번의 속성이 target으로 전파됨
            if arr[i] == win:
                next_arr[target] = arr[i]

        # 한 초 동안의 변화를 한꺼번에 반영
        arr = next_arr

    return arr