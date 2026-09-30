# 기출 1: 타일 뒤집기
# 소요시간: 30분 / 시도: 2회

# 효율적인 타일 배치로 안전하게 통과하기?
n = 10 #타일 개수
h1 = 0 
h2 = 50
c1 = -50
c2 = 0
temperature = [30, -20, -5, 10, 31, -50]


#초기 설정
min_t = (h1*n + c1* 0) /n 
max_t = (h2*n + c1* 0) /n
c_num = 0
result = 0

#리스트만들어서 전체 범위값 생성후에 진행할까 했는데, 우선 계속 계산하는 방식으로
#경로 문제로 풀어볼까?
for t in temperature:
    if min_t <= t <= max_t:
        continue

    else:
        if t > min_t:
            for i in range(c_num, -1, -1):
                min_t = (h1*(n-i) + c1*i) /n
                max_t = (h2*(n-i) + c2*i) /n

                if min_t <= t <= max_t:
                    result += c_num-i
                    c_num = i
                    break

        elif t < max_t:
            for i in range(c_num, 11):
                min_t = (h1*(n-i) + c1*i) /n
                max_t = (h2*(n-i) + c2*i) /n
                    
                if min_t <= t <= max_t:
                    result += i-c_num
                    c_num = i
                    break

print(result)