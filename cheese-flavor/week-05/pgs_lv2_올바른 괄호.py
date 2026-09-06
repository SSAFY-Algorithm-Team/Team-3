# 프로그래머스 Lv2. 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 소요시간: 10분 / 시도: 1회


def solution(s):
    
    # 시작값부터 ( 아니면 false
    if s[0] == ')':
        return False

    else:
        # 새 배열에 값을 추가하면서 반복적으로 확인
        arr = []
    
        for i in range(len(s)):
            arr += s[i]
            
            if len(arr) >= 2:
                if arr[-2]+arr[-1] == '()':
                    # 뒤에 두개 제거
                    arr.pop()
                    arr.pop()
                
        if len(arr) == 0:
            return True
        
        else:
            return False


    
            
            
            
        
    


