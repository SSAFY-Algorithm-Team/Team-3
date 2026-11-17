# 코드트리 2-4-3-01. 블럭쌓는 명령2 (Easy)
# 출처: CodeTree
#
# [구간 시뮬레이션]
# 명령으로 주어진 구간을 배열에서 직접 순회하며 값을 누적하는 방식
# 문제의 칸 번호는 1부터 시작하지만, 파이썬 배열 인덱스는 0부터 시작하므로 a - 1부터 접근
# range(a - 1, b)는 종료값 b를 포함하지 않으므로 문제의 b번 칸까지 처리 가능
#
# [구간 누적]
# arr[i] += 1 : 해당 칸에 블럭을 하나 추가하고, 여러 명령이 겹치면 누적
# max(arr) : 모든 칸의 블럭 개수 중 최댓값 확인

n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# [배열 초기화] 각 칸의 블럭 개수 0으로 초기화
arr = [0] * n

# [구간 누적] 명령에 해당하는 구간에 블럭 1개씩 추가
for a, b in commands:
    for i in range(a - 1, b):
        arr[i] += 1

print(max(arr))
