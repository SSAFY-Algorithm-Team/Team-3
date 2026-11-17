# 코드트리 Trail2. 개발팀의 능력
# https://www.codetree.ai/ko/trails/complete/curated-cards/test-the-capabilities-of-the-development-team/description

arr = list(map(int, input().split()))

# Please write your code here.
total = sum(arr)
ans = float('inf')

for i in range(5):
    for j in range(i + 1, 5):
        for k in range(5):
            for l in range(k + 1, 5):
                # 두 번째 팀이 첫 번째 팀과 사람이 겹치면 안 됨
                if k == i or k == j or l == i or l == j:
                    continue

                t1 = arr[i] + arr[j]
                t2 = arr[k] + arr[l]
                t3 = total - t1 - t2

                # 세 팀 능력치가 모두 달라야 함
                if t1 == t2 or t2 == t3 or t1 == t3:
                    continue

                ans = min(ans, max(t1, t2, t3) - min(t1, t2, t3))

if ans != float('inf'):
    print(ans)
else:
    print(-1)
