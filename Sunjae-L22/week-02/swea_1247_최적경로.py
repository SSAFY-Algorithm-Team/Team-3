# SWEA D5. 최적경로
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15OZ4qAPICFAYD
# 소요시간: 80분 / 시도: 2회

T = int(input())


# 두 점 사이의 거리 구하는 함수
def dist(loc_1, loc_2):
    loc_1_x, loc_1_y = loc_1[0], loc_1[1]
    loc_2_x, loc_2_y = loc_2[0], loc_2[1]
    return abs(loc_1_x - loc_2_x) + abs(loc_1_y - loc_2_y)


# 사무실, 집, 고객 좌표 받으면 최적 경로 반환하는 함수
def best_path(office, home, customers):
    start_x, start_y = office[0], office[1]
    end_x, end_y = home[0], home[1]
    customer_n = len(customers)
    visited = [False] * customer_n
    result = []
    # 극단적으로 10명이 (0, 0), (100, 100)에 5명씩 있고 와리가리하면 2200이 최대
    path_len = 2201
    
    
    # 몇개 방문했는지, 현재 경로길이, 전에 방문한 곳
    def dfs(depth, candidate, before):
        if depth == customer_n:
            candidate += dist(before, home)
            result.append(candidate)
            # path_len = min(path_len, candidate)
            
        for i in range(customer_n):
            if visited[i]:
                continue
            candidate += dist(before, customers[i])
            # 가지치기(1)
            # if candidate > path_len:
            #     continue
            visited[i] = True
            dfs(depth+1, candidate, customers[i]) 
            # 되돌리기
            visited[i] = False
            candidate -= dist(before, customers[i])   
            
    dfs(0, 0, office)
    return min(result)


for tc in range(1, T+1):
    N = int(input())
    
    # 전체 좌표 받아서 회사 좌표, 집 좌표, 고객 좌표로 나누기
    all_list = list(map(int, input().split()))
    office = (all_list[0], all_list[1])
    home = (all_list[2], all_list[3])
    customers = []
    
    for i in range(N):
        x = all_list[4 + i*2]
        y = all_list[5 + i*2]
        customers.append((x, y))
        
    print(f"#{tc} {best_path(office, home, customers)}")