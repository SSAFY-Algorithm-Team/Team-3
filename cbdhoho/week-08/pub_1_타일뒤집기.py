n = int(input())
h1, h2, c1, c2 = map(int, input().split())
temperature = list(map(int, input().split()))

h_cnt = n
c_cnt = n - h_cnt
total_cnt = 0

for temp in temperature:
    while True:
        
        min_temp = (h1*h_cnt+c1*c_cnt)/n
        max_temp = (h2*h_cnt+c2*c_cnt)/n

        if (min_temp <= temp <= max_temp):
            break
        # temp가 mintemp 보다 작으면
        if min_temp > temp:
            if h1 < c1:
                h_cnt += 1
                c_cnt -= 1
            else:
                h_cnt -= 1
                c_cnt += 1
            total_cnt += 1

        if max_temp < temp:
            if h2 > c2:
                h_cnt += 1
                c_cnt -= 1
            else:
                h_cnt -= 1
                c_cnt += 1
            total_cnt += 1

print(total_cnt)    