# ==============================================
# 코드 제출시 아래 2줄은 반드시 주석처리 하여 제출
# import sys
# sys.stdin = open('algo2_sample_in.txt')
# ==============================================

# 아래에 코드를 작성하세요.
from collections import defaultdict
from itertools import permutations
T = int(input())

for tc in range(1, T+1):
    # 정보 입력받기
    N = int(input())
    workable = defaultdict()
    for i in range(N):
        workable[i] = defaultdict()
        line = list(map(int, input().split()))
        for j in range(len(line)):
            if line[j] > 0:
                workable[i][j] = line[j]

    # 가능한지 확인 -> 길어봤자 N**2 : 100번
    work_finished = [False] * N
    for people in workable.values():
        for work_n in people:
            work_finished[work_n] = True
    if sum(work_finished) != N:
        answer = -1
    else:
        # 가능하다고 판별되면 가장 짧은 거 찾아보자(최대시간은 1000을 못넘김)
        answer = 1001
        for perm in permutations(range(N), N):
            time = 0
            flag = False
            for people, work_n in enumerate(perm):
                if work_n not in workable[people].keys():
                    flag = True
                    continue
                time += workable[people][work_n]
                if time > answer:
                    flag = True
                    continue
            if flag:
                continue
            answer = min(answer, time)

    print(f"#{tc} {answer}")