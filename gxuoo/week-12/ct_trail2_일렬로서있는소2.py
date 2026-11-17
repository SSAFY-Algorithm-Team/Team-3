# 코드트리 Trail2. 일렬로 서있는 소 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-cattle-in-a-rowing-up-2/description

N = int(input())
A = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[i] <= A[j] <= A[k]:
                cnt += 1

print(cnt)
