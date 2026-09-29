# 기출 3. 정상 거래 개수
# 소요시간: 5분  시도횟수: 1회
transactions = [
[100, 100, 5000, 5000],
[200, 190, 8000, 8000],
[150, 150, 7000, 6900],
[300, 300, 12000, 12000]
]

#약정증권수량, 전달된증권수량, 약정대금, 지급된대금


def sol(transactions):
    count = 0
    for transaction in transactions:
        contractedQty = transaction[0]
        deliveredQty = transaction[1]
        contractAmt = transaction[2]
        paidAmt = transaction[3]

        if contractedQty == deliveredQty and contractAmt == paidAmt:
            count += 1

    return count

result = sol(transactions)
print(result)