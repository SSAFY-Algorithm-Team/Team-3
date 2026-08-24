# 프로그래머스 Lv2. 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# dfs
# 돌 때 +로 끝까지 탐색하고, 타겟이 아니라면 리턴 후 -로 탐색
# count는 if sum == target일 때 answer += 1

# 

def solution(numbers, target):
    answer = 0 
    def dfs(sum, depth):
        nonlocal answer 
        # 깊이가 마지막이고, sum이 타겟과 같을 때 카운트 +1
        if depth == len(numbers):
            if sum == target: 
                answer += 1
                return
            return      
         
        # dfs 매개변수로 더해줄 숫자를 보내줘야할 거 같은데, 
        # 돌고 나서 -로 빠져나오는게 넘 어려운 듯
        dfs(sum + numbers[depth], depth + 1)
        dfs(sum - numbers[depth], depth + 1)

    dfs(0, 0)
    return answer

solution([4,1,2,1], 4)