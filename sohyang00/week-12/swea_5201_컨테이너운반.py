import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())

for testCase in range(1, T+1):
    N, M = map(int, input().split()) #컨테이너, 트럭

    containers = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks = list(map(int, input().split()))
    trucks.sort(reverse=True)

    weight = 0
    # 어라? 둘 다 같이 돌아가야하는데 이중 포문이 되면 안되는 거 아냐...? 
    i, j = 0, 0
    while True:
        if i == N: #컨테이너
            break
        if j == M: #트럭
            break

        if trucks[j] >= containers[i]:
            weight += containers[i]
            i += 1
            j += 1
        else:
            i += 1
    print(f'#{testCase} {weight}')
    