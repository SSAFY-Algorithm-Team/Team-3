# 프로그래머스 Lv2. 타겟 넘버
# http://school.programmers.co.kr/learn/courses/30/lessons/43165
# 소요시간: 25분 / 시도: 2회

#순열로만 풀다가 갑자기 이거 푸니까 방법을 까먹음

def solution(numbers, target):
    
    # 너무 어렵게 생각해서 당함
    
    answer = 0
    
    def dfs(idx, num):        
        nonlocal answer #-> 값이 변하는것을 담기 위해서 / 그냥 읽기용이면 nonlocal 필요없음
        
        if idx == len(numbers):
            if num == target:
                answer += 1 #-> 값이 변하는것을 출력하기 위해서는 nonlocal을 사용 /
            return  # return answer를 안써도 되는 이유? => 전역 변수이므로 함수 내에서 직접 수정 가능 그래서 return만 진행
        
        # for문을 idx로 대체
        dfs(idx +1, num + numbers[idx])
        dfs(idx +1, num - numbers[idx])
    
    dfs(0, 0)
    
    return answer