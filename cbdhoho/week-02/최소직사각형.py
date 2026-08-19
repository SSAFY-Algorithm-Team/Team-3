def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    max_w = float('-inf')
    max_h = float('-inf')
    for w, h in sizes:
        if max_w < w:
            max_w = w
        if max_h < h:
            max_h = h
    answer = max_w * max_h
    return answer