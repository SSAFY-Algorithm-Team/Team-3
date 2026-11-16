# 코드트리 Trail2. 괄호 쌍 만들어주기 3
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-pair-parentheses-3/description

A = input()

# Please write your code here.
cnt = 0
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] == '(' and A[j] == ')':
            cnt += 1

print(cnt)
