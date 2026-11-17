import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for testCase in range(1, T+1):
    N, M, K = map(int, input().split())
    # 전체 문제, 맞춘 문제, 카운터
    nums = [0]* (N+1)
    k_count = 0
    fail_count = N - M
    score = 0
    if N != M:    
        for i in range(len(nums)-K, 0, -K):
            nums[i] = -1
            k_count += 1
            if k_count == fail_count:
                break
    if k_count != fail_count:
        minus = fail_count - k_count 
        i = 1
        while minus:
            if nums[i] != -1:
                nums[i] = -1
                i += 1
                minus -= 1
            else:
                i += 1

    k_count = 0
    for i in range(1, N+1):
        if nums[i] == -1:
            k_count = 0
        elif k_count == K-1:
             k_count = 0
             score += 1
             score *= 2
        else: 
            score += 1
            k_count += 1
    #print("score:", score, "k_count:", k_count)
    print(f'#{testCase} {score}')