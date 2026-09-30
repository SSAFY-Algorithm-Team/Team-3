def solution(n, h1, h2, c1, c2, temperature):
    answer = 0
    now = 0  # 현재 C면 개수

    for temp in temperature:
        possible = []

        # 이 온도를 버틸 수 있는 C면 개수 찾기
        for c in range(n + 1):
            h = n - c

            low = h1 * h + c1 * c
            high = h2 * h + c2 * c

            if low <= temp * n <= high:
                possible.append(c)

        # 가능한 C면 개수의 범위
        left = possible[0]
        right = possible[-1]

        # 현재 상태로 못 버티면 가장 가까운 곳까지만 뒤집기
        if now < left:
            answer += left - now
            now = left

        elif now > right:
            answer += now - right
            now = right

    return answer