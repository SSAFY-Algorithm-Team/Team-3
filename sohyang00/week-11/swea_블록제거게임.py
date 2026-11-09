import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())

#블럭 찾는 함수
def search(blocks, curr_score):
    global max_score
    if not blocks:
        max_score = max(max_score, curr_score)
        return
    
    for i in range(len(blocks)):
        add_score = get_score(blocks, i)
        next_blocks = blocks[:i] + blocks[i+1:]
        search(next_blocks, curr_score + add_score)

#블록을 부셔서 얻을 스코어
def get_score(blocks, i):
    if len(blocks) == 1:
        return blocks[i]
    elif i == 0:
        return blocks[1]
    elif i == len(blocks) -1:
        return blocks[i-1]
    return blocks[i-1] * blocks[i+1]

for testCase in range(1, T+1):
    n = int(input())
    blocks = list(map(int,input().split()))
    max_score = 0

    search(blocks, 0)

    print(f'#{testCase} {max_score}')
