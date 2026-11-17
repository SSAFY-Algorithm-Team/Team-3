# 코드트리 Trail2. 괄호 쌍 만들어주기 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-pair-parentheses-2/description

A = input()

# Please write your code here.
total = 0
for i in range(len(A) - 1):
    cnt = 0
    if A[i] == '(' and A[i + 1] == '(':
        for j in range(i, len(A) - 1):
            if A[j] == ')' and A[j + 1] == ')':
                cnt += 1
    
    total += cnt

print(total)
