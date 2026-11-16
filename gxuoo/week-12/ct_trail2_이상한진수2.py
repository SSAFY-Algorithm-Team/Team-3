# 코드트리 Trail2. 이상한 진수 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-awkward-digits-2/description

a = input()

# Please write your code here.
a = list(a)
flag = False
for i in range(len(a)):
    if a[i] == '0':
        a[i] = 1
        flag = True
        break

if not flag:
    a[-1] = '0'

res, i = 0, 1
for j in range(len(a) - 1, -1, -1):
    res += int(a[j]) * i
    i *= 2

print(res)
