import sys
sys.stdin = open("sample_input.txt", "r")

from collections import deque

def bfs(start):
    bigQ = deque([start])
    cnt = 0
    while bigQ:
        idx = bigQ.popleft()

        for nxt in bigger[idx]:
            if not visited[nxt]:
                visited[nxt] = True
                bigQ.append(nxt)
                cnt += 1

    smlQ = deque([start])
    while smlQ:
        idx = smlQ.popleft()      
        for nxt in smaller[idx]:
            if not visited[nxt]:
                visited[nxt] = True
                smlQ.append(nxt)
                cnt += 1  
    if cnt == N-1:
        return 1
    else:
        return 0 #전부 찾지 못햇으면 0, 찾았다면 1


T = int(input())
for testCase in range(1, T+1): 
    N = int(input())
    M = int(input())
    bigger = [[]*(N) for _ in range(N+1)]
    smaller = [[]*(N) for _ in range(N+1)]

    for _ in range(M):
        i, j = map(int, input().split())
        # i는 j보다 키가 작다
        # 각 idx에는 자기자신보다 키가 큰 idx가 들어있음
        bigger[i].append(j) 
        smaller[j].append(i)

    count = 0
    for idx in range(1,N+1):
        visited = [False]*(N+1)
        count += bfs(idx)
    print(f'#{testCase} {count}')
