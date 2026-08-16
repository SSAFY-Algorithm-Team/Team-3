# 프로그래머스 Lv2. 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 소요시간: 20분 / 시도: 2회

# 배열에서 길이 m짜리 순열 -> 던전 돌 순서 뽑기
def permutations(arr, m):
    result, path, used = [], [], [False] * len(arr)

    def dfs(depth):
        if depth == m:
            result.append(path[:])
            return
        for i in range(len(arr)):
            if used[i]:
                continue
            used[i] = True
            path.append(arr[i])
            dfs(depth+1)
            path.pop()
            used[i] = False

    dfs(0)
    return result


def solution(k, dungeons):
    answers = []
    dungeon_n = len(dungeons)
    explore_sequences = permutations(range(dungeon_n), dungeon_n)

    # 던전 도는 순서
    for explore_sequence in explore_sequences:
        # 순서 순열 돌때마다 remain_hp를 받아온 k로 초기화
        remain_hp = k
        answer = 0

        for i in explore_sequence:
            if remain_hp < dungeons[i][0]:
                continue
            remain_hp -= dungeons[i][1]
            answer += 1

        answers.append(answer)

    return max(answers)
