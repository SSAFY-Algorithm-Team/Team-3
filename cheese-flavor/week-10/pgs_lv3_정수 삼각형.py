# 프로그래머스 Lv3. 정수 삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 소요시간: 60분 / 시도: 3회


# 규칙 정해서 그냥 for문 돌리는거구만

def solution(triangle):
    n = len(triangle)
    
    #처음에 DP라는 새 배열을 만들었다가 그냥 지우고 기존 배열에서 진행
    
    for i in range(1, n):
        for j in range(i+1):
        
            # 방향성을 3개로 두고 나누어서 진행
            # 왼쪽 일자로 구하고, 오른쪽도 일자로 구하고 (바로 윗값만 쓰니까)
            # 가운데에서는 (-1, -1)값과 (-1, 0) 위치값만 활용하면 되니까
            
            # 1. 왼쪽 끝
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
                
            # 2. 오른쪽 끝 
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
                
            # 3. 가운데(두 값 중에 큰것만 쓰면 되니까)  
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
                
    return max(triangle[-1])


    
            
            
            
        
    


