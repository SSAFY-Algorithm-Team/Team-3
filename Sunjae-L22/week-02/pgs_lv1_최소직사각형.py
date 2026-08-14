# 프로그래머스 Lv1. 최소직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 소요시간: 20분 / 시도: 1회

def solution(sizes):
    answer = 0
    max_len = 0
    standard = []
    # 가장 긴 길이 찾기(w, h 중에)
    for size in sizes:
        if size[0] > max_len:
            max_len = size[0]
            standard = ['w', size[1]]
        if size[1] > max_len:
            max_len = size[1]
            standard = ['h', size[0]]

    if standard[0] == 'w':
        # h 중에 기준보다 높은데 그 행의 w가 h보다 작다면 바꾸는게 이득
        for i in range(len(sizes)):
            if sizes[i][1] > standard[1] and sizes[i][0] < sizes[i][1]:
                sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    if standard[0] == 'h':
        # 반대
        for i in range(len(sizes)):
            if sizes[i][0] > standard[1] and sizes[i][0] > sizes[i][1]:
                sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    ws , hs = [], []
    for size in sizes:
        ws.append(size[0])
        hs.append(size[1])

    answer = max(ws) * max(hs)



    return answer