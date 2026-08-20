# nonlocal은 항상 맨 위에 선언되어야함,, 가지치기 아래에다가 선언했다가 오류남.(당연한거지만)

def solution(numbers, target):
    answer = 0
    cnt = 0
    # numbers의 index, 최종적으로 나오게 될 숫자
    def dfs(idx, result):
        nonlocal cnt
        # 마지막 인덱스면
        if idx == len(numbers):
            # 타겟 넘버면
            if result == target:
                cnt += 1
            return
        
        num = numbers[idx]
        # 더하는 방식
        dfs(idx+1, result+num)
        # 빼는 방식
        dfs(idx+1, result-num)
    dfs(0, 0)
    answer = cnt
    return answer