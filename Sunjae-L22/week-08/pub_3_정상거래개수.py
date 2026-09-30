# 소요 시간 : 5분

transactions = [
    [100, 100, 5000, 5000],   
    [200, 190, 8000, 8000],   
    [150, 150, 7000, 6900],   
    [300, 300, 12000, 12000]  
]
answer = 0

for agreed_qty, delivered_qty, agreed_amount, paid_amount in transactions:
    if agreed_qty == delivered_qty and agreed_amount == paid_amount:
        answer += 1

print(answer)