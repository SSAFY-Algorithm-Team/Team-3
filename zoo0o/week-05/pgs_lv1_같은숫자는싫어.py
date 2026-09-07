# 프로그래머스 Lv1. 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 소요시간: 3분 / 시도: 1회

def solution(arr):
    # 1. 첫 번째 숫자는 미리 저장
    answer = [arr[0]]
    idx = 0

    for i in range(1, len(arr)):
        # 2. 이전에 저장한 숫자와 현재 숫자가 다를 때만 추가
        if answer[idx] != arr[i]:
            answer.append(arr[i])
            idx += 1

    return answer