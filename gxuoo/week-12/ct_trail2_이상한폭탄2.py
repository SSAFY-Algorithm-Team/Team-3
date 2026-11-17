# 코드트리 Trail2. 이상한 폭탄 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-strange-bomb-2/description

N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
max_num = -1
for i in range(N):
    for j in range(i + 1, N):
        if num[i] == num[j] and abs(i - j) <= K:
            max_num = max(max_num, num[i])

print(max_num)
