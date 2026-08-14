# SWEA 1289. 원재의 메모리 복구하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN
# 소요시간: 15분 / 시도: 1회

T = int(input())
for test_case in range(1, T + 1):
    memory = input()
    count = 0
    possible = True
    
    for i in range(len(memory)):
        if int(memory[i]) == 1 and possible:
            count += 1
            possible = False
            
        elif int(memory[i]) == 0 and not possible:
            count += 1
            possible = True
    
    print(f"#{test_case} {count}")