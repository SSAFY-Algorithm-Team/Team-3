# 코드트리 Trail2. 스승의 은혜 2
# https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-the-grace-form-teacher-2/description

N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.
ans = 0

for i in range(N):
    total, cnt = 0, 0
    arr = P[:]
    arr[i] = arr[i] // 2
    arr.sort()
    for j in range(N):
        if total + arr[j] <= B:
            total += arr[j]
            cnt += 1
        else:
            break

    ans = max(ans, cnt)

print(ans)