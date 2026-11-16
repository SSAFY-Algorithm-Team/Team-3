# 코드트리 Trail2. 특정 구간의 원소 평균값
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-elemental-mean-value-for-a-particular-interval/description

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range(n):
    for j in range(i, n):
        part = arr[i:j + 1]
        total = sum(part)
        length = j - i + 1

        if any(x * length == total for x in part):
            cnt += 1

print(cnt)
