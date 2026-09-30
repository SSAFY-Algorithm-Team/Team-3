# 소요시간 : 25분

# H면이 a개, C면이 b개 (a + b = n)

# a, b개가 주어지면 온도 범위 뱉는 함수
def temp_range(a, b, h1, h2, c1, c2, n):
    low = (h1 * a + c1 * b) / n
    high = (h2 * a + c2 * b) / n
    return low, high


n = int(input())
h1, h2, c1, c2 = map(int, input().split())
temp_list = list(map(int, input().split()))

a, b = n, 0
answer = 0
for temp in temp_list:
    low, high = temp_range(a, b, h1, h2, c1, c2, n)
    if low <= temp and temp <= high:
        continue
    else:
        # direction: H면 개수(a)를 늘리면 +1, 줄이면 -1
        if temp < low:
            # low를 낮춰야됨 
            direction = -1 if h1 > c1 else 1
        else:
            # high를 높여야됨
            direction = 1 if h2 > c2 else -1

        while not (low <= temp <= high):
            # 해당 방향으로 더 뒤집을 타일이 없으면 통과 불가능
            if not (0 <= a + direction <= n):
                answer = -1
                break

            # direction이 1이면 a는 늘리고 b는 줄임
            # direction이 -1d이면 반대
            a += direction
            b -= direction
            answer += 1

            # a, b 바뀌었으니까 범위 다시 계산
            low, high = temp_range(a, b, h1, h2, c1, c2, n)

        if answer == -1:
            break

print(answer)