# 코드트리 Trail2. 팰린드롬 수 찾기
# https://www.codetree.ai/ko/trails/complete/curated-cards/test-find-the-number-of-palindrome/description

X, Y = map(int, input().split())

# Please write your code here.
total = 0
for i in range(X, Y + 1):
    arr = list(str(i))
    cnt = 0
    for j in range(len(arr)):
        if arr[j] == arr[len(arr) - j - 1]:
            cnt += 1

    if cnt == len(arr):
        total += 1

print(total)
