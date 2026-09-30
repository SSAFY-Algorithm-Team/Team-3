transactions = [
    [100, 100, 5000, 5000],
    [200, 190, 8000, 8000],
    [150, 150, 7000, 6900],
    [300, 300, 12000, 12000]
]

cnt = 0

for t in transactions:
    if t[0] == t[1] and t[2] == t[3]:
        cnt += 1

print(cnt)