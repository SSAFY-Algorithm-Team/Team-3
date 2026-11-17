# 코드트리 Trail2. 아름다운 수열 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-beautiful-sequence-2/description

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
sorted_b = sorted(B)
total = 0
for i in range(N - M + 1):
    if sorted(A[i:i + M]) == sorted_b:
        total += 1

print(total)
