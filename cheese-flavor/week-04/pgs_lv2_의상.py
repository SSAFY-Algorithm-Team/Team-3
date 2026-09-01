# 프로그래머스 Lv2. 의상
# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 소요시간: 20분 / 시도: 2회


def solution(clothes):
    count = {}
    
    # 전체 가짓수에서 아무것도 안 입으면 모든 조합
    for name, kind in clothes:
        if kind not in count:
            count[kind] = 1
        else:
            count[kind] += 1
        
    answer = 1
    for kind in count:
        answer *= (count[kind] + 1)
        
    return answer - 1


''' dfs 저주에 갖힘
def solution(clothes):
    cloth = []
    cloth_count = []
    visited = [False] * len(clothes)
    
    for i in range(len(clothes)):
        if clothes[i][1] not in cloth:
            cloth.append(clothes[i][1])
            cloth_count.append(1)
        else:
            for j in range(len(clothes)):
                if clothes[i][1] == cloth[j]:
                    cloth_count[j] += 1
                    break
    answer = sum(cloth_count)
    
    
    
    if len(cloth_count) > 1:
        for i in range(len(cloth_count)):
            for j in range(len(cloth_count)):
                
        

    return cloth_count
'''