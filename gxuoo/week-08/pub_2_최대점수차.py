# 기출 2. 최대 점수 차
# 소요시간: 5분 / 시도: 1회

def solution(arr):
    # 최대 경기 수 구하기
    N = arr[0][0]

    for score in arr:
        if score[0] >= N:
            N = score[0]

    # 결과 저장 배열
    result = [0] * N

    # 득점할 때마다 점수 차를 구해서 최댓값 갱신
    answer = 0

    for score in arr:
        result[score[0] - 1] += score[1]
        answer = max(answer, max(result) - min(result))

    return answer

if __name__ == "__main__":
    print(solution([
        [1, 2],
        [2, 3],
        [3, 1],
        [4, 5],
        [2, 3],
        [1, 4]
    ]))  # 5
