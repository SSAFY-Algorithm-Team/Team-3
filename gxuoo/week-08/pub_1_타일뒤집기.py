# 기출 1. 타일 뒤집기 ⭐
# 소요시간: / 시도:


def solution(n, h1, h2, c1, c2, temperature):
    answer = 0

    # H면이 a개일 때 견딜 수 있는 범위
    def get_range(a):
        b = n - a
        return h1 * a + c1 * b, h2 * a + c2 * b

    # 처음엔 전부 H면
    a = n

    for t in temperature:
        lo, hi = get_range(a)
        if lo <= t * n <= hi:
            continue

        # 안전한 a 중 현재와 가장 가까운 값으로 이동
        best = None
        for next_a in range(n + 1):
            lo, hi = get_range(next_a)
            if lo <= t * n <= hi and (best is None or abs(next_a - a) < abs(best - a)):
                best = next_a

        # 어떤 상태로도 견딜 수 없는 온도
        if best is None:  
            return -1
        answer += abs(best - a)
        a = best

    return answer


if __name__ == "__main__":
    print(solution(
        10, 0, 50, -50, 0,
        [30, -20, -5, 10, 31, -50]
    ))  # 12
