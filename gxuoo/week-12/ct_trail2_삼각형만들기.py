# 코드트리 Trail2. 삼각형 만들기
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-create-triangle/description

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # x축 평행 변: y가 같은 두 점 / y축 평행 변: x가 같은 두 점
            has_x_parallel = (y[i] == y[j] or y[j] == y[k] or y[i] == y[k])
            has_y_parallel = (x[i] == x[j] or x[j] == x[k] or x[i] == x[k])
            if not (has_x_parallel and has_y_parallel):
                continue

            # 신발끈 공식 (넓이의 2배)
            area2 = abs(x[i] * y[j] + x[j] * y[k] + x[k] * y[i]
                        - x[j] * y[i] - x[k] * y[j] - x[i] * y[k])
            ans = max(ans, area2)

print(ans)
