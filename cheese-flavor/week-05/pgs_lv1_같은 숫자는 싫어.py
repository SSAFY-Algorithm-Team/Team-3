# 프로그래머스 Lv1. 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 소요시간: 10분 / 시도: 1회


def solution(arr):
    answer = []
    
    for i in arr:
        
        # 초기값이 없으면 넣기
        if len(answer) == 0:
            answer.append(i)

        #연속이니까 마지막 값이랑 다르면 넣기
        else:
            if answer[-1] != i:
                answer.append(i)                
    
    return answer