# 코드트리 Trail2. Carry 피하기 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-escaping-carry-2/description

n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
def is_carried(a, b, c):
    while a or b or c:
        if (a % 10 + b % 10 + c % 10) >= 10:
            return True
        else:
            a //= 10
            b //= 10
            c //= 10
    
    return False

res = -1
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if (arr[i] % 10 + arr[j] % 10 + arr[k] % 10) >= 10:
                continue
            else:
                if not is_carried(arr[i], arr[j], arr[k]):
                    res = max(res, (arr[i]+arr[j]+arr[k]))

print(res)
