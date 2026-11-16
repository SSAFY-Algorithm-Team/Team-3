# 코드트리 Trail2. 씨 오 더블유 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-c-o-w-2/description

n = int(input())
S = input()

# Please write your code here.
total = 0
for i in range(n):
    cnt = 0
    if S[i] == 'C':
        for j in range(i, n):
            if S[j] == 'O':
                for k in range(j, n):
                    if S[k] == 'W':
                        cnt += 1

    total += cnt

print(total)
