# SWEA 6190. 정곤이의 단조 증가하는 수
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWcPjEuKAFgDFAU4
# 소요시간: 15분 / 시도: 1회

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    num = list(map(int, input().split()))
    m_num = []
    possible = False
    
    for i in range(0, n-1):
        for j in range(i+1, n):
            m_num.append(num[i] * num[j])
    m_num.sort(reverse = True)
    #print(f"#{test_case} {''.join(sorted(str(m_num[0])))}")  확인용
    
    for n in m_num:
        if not possible and str(n) == ''.join(sorted(str(n))):
            print(f"#{test_case} {n}")
            possible = True
            
    if not possible:
        print(f"#{test_case} -1")