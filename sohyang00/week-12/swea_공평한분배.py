import sys
sys.stdin = open("sample_input.txt", "r")
from itertools import permutations
# 순열 쓰려고 했는데, 굳이 써야할까? 라는 생각이 조금 들었다.

T = int(input())

for testCase in range(1,T+1):
    N, K = map(int, input().split())
    candys = list(map(int, input().split()))
    candys.sort()
    result = candys[K-1] - candys[0] #초기값도 대충 99999999 이렇게 적었다가 틀림 
    for i in range(N-K+1):
        result = min(result, candys[i+K-1] - candys[i])
    print(f'#{testCase} {result}')

# 처음에 생각했던 것, 근데 틀림
#for testCase in range(1,T+1):
#    N, K = map(int, input().split())
#    candys = list(map(int, input().split()))
#    candys.sort()
#    result = 0
#
#    if N == K:
        #result = candys[-1] - candys[0]
#    else:
        #result = candys[len(candys)-1-(N-K)] - candys[0]
#    print(f'#{testCase} {result}')