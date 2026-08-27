# 프로그래머스 Lv2. 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 소요시간: 50분 / 시도: 2회

def solution(numbers):
    n = len(numbers)
    visited = [False] * n # 각 숫자 활용여부
    result = 0
    new_numbers = set() # 중복제거용


    # DFS 로직이 기억 잘 안남
    def dfs(path):
        if path and int(path) >= 2:
            new_numbers.add(int(path)) #계속해서 초기값 추가
            
        for i in range(n): # 순서를 돌아가겠다는 형태
            if not visited[i]:
                visited[i] = True
                dfs(path+numbers[i])
                visited[i] = False
                
    dfs("")
    #return len(new_numbers) 확인용
    
    for i in new_numbers:
        possible = True   #그냥 파시블 사랑함 청년
        
        # 다른 로직 분명있었는데 2기준 절반이상은 안넘으니까 난 이렇게 할게용
        # 로그 n으로 진행하면 더 빠름! => 앞으로 이거 사용하기
        for j in range(1, (i//2)): 
            if i % (j+1) == 0:
                possible = False
        if possible:
            result += 1

    return result

'''
# 일부테스트에서 죽다 살아남
테스트 2 〉	통과 (6768.87ms, 11.8MB)
테스트 10 〉통과 (7141.37ms, 11.6MB)
'''

    