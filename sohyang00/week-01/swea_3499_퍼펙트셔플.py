import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = input().split()
    state = 'even'
    if n%2 == 1:
        mid = n//2+1
        state = 'odd'
    else: 
        mid = n//2
    
    result = []

    if state == 'odd':
        for i in range(mid-1):
            result.append(arr[i])
            result.append(arr[mid+i])
        result.append(arr[mid-1])
    else:
        for i in range(mid):
            result.append(arr[i])
            result.append(arr[mid+i])
        

    result = ' '.join(result)

    print(f'#{test_case} {result}')