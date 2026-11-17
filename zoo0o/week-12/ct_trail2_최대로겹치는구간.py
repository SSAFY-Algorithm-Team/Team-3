# 코드트리 2-4-3-02. 최대로 겹치는 구간 (Medium)
# 출처: CodeTree
#
# [구간 시뮬레이션]
# 선분이 차지하는 작은 구간을 배열에 표시하고, 겹치는 횟수를 누적하는 방식
#
# [끝점 제외]
# 선분 [x1, x2]가 차지하는 구간은 x1부터 x2 - 1까지
# range(x1, x2)는 종료값을 포함하지 않으므로 끝점에서만 만나는 선분은 겹침으로 계산하지 않음
#
# [좌표 변환]
# 배열 인덱스는 음수를 그대로 좌표로 사용할 수 없으므로 OFFSET을 더해 양수 인덱스로 변환
# 좌표 범위가 -100부터 100까지이므로 OFFSET은 100

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

OFFSET = 100
arr = [0] * 201

for x1, x2 in segments:
    for i in range(x1 + OFFSET, x2 + OFFSET):
        arr[i] += 1

print(max(arr))
