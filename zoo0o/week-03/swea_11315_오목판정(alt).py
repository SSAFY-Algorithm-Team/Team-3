# 내 풀이: DFS + visited + 백트래킹으로 가능한 경로를 하나씩 탐색
# 정석 풀이: 오일러 경로를 이용해 모든 항공권을 정확히 한 번씩 사용

from collections import defaultdict


def solution(tickets):
    # 오일러 경로:
    # 그래프의 모든 간선(여기서는 항공권)을 정확히 한 번씩 사용하는 경로
    #
    # 공항 = 정점
    # 항공권 = 간선
    #
    # 이 문제는 "모든 항공권을 반드시 사용"해야 하므로
    # 오일러 경로 문제로 볼 수 있다.

    graph = defaultdict(list)

    # pop()은 리스트의 마지막 값을 꺼내므로
    # 알파벳이 빠른 공항을 마지막에 두기 위해 역순 정렬
    tickets.sort(reverse=True)

    # 출발 공항별로 갈 수 있는 도착 공항 저장
    #
    # 예:
    # ICN -> SFO
    # ICN -> ATL
    #
    # graph["ICN"] = ["SFO", "ATL"]
    # pop()하면 "ATL"부터 꺼내짐
    for start, end in tickets:
        graph[start].append(end)

    route = []

    def dfs(current):
        # 현재 공항에서 아직 사용하지 않은 항공권이 있다면
        # 하나를 꺼내서 그 도착 공항으로 이동
        while graph[current]:
            # 항공권 하나 사용
            # pop()으로 꺼냈으므로 같은 항공권을 다시 사용할 수 없음
            next_airport = graph[current].pop()

            # 다음 공항에서도 계속 항공권을 사용하며 이동
            dfs(next_airport)

        # 여기까지 왔다는 것은
        # 현재 공항에서 더 이상 사용할 수 있는 항공권이 없다는 뜻
        #
        # 이때 현재 공항을 route에 추가한다.
        #
        # 즉, 갈 때 추가하는 것이 아니라
        # "더 이상 갈 곳이 없어서 돌아올 때" 추가한다.
        #
        # 그래서 route에는 최종 경로가 거꾸로 저장된다.
        route.append(current)

    # 문제에서 항상 ICN에서 출발한다고 했으므로 ICN부터 탐색
    dfs("ICN")

    # route는 뒤에서부터 저장되므로 마지막에 뒤집는다.
    return route[::-1]
