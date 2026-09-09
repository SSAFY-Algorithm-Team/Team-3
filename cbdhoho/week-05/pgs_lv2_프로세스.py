from collections import deque

def solution(priorities, location):
    queue = deque()
    for idx, p in enumerate(priorities):
        queue.append([idx, p])
    
    result = []
    while queue:
        idx, p = queue.popleft()
        # 이 중에 참인게 하나라도 있다면!!! -> True // all()은 전부 다 참이어야함!
        if any(p < other[1] for other in queue):
            queue.append([idx, p])
        else:
            result.append(idx)
        
    return result.index(location) + 1