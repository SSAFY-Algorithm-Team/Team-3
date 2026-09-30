# 기출 3. 정상 거래 개수
# 소요시간: 2분 / 시도: 1회

def solution(transactions):
    answer = 0

    for ts in transactions:
        if ts[0] == ts[1] and ts[2] == ts[3]:
            answer += 1
    
    return answer


if __name__ == "__main__":
    # [약정 증권 수량, 전달된 증권 수량, 약정 대금, 지급된 대금]
    print(solution([
        [100, 100, 5000, 5000],
        [200, 190, 8000, 8000],
        [150, 150, 7000, 6900],
        [300, 300, 12000, 12000],
    ]))  # 2
