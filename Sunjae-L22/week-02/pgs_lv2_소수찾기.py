# 프로그래머스 Lv2. 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 소요시간: 90분 / 시도: 3회

def solution(numbers):
    answer = 0
    
    # 문자열 numbers를 정수 배열로 변환
    int_numbers = []
    for number in numbers:
        int_numbers.append(int(number))

    perm_list = []
    # 길이 1부터 배열 길이까지의 순열조합 모두 확인
    for i in range(1, len(int_numbers)+1):
        perm_list.append(permutation(int_numbers, i))
    
    nums = []
    for perms in perm_list:
        for perm in perms:
            num = 0
        # 뒤에서부터 차례대로 1, 10, 100곱해서 숫자 만들기
            for i in range(len(perm)):
                num += (int(perm[len(perm) - i - 1])) * (10 ** i)
            nums.append(num)
    nums = set(nums)
    for i in nums:
        if is_it_prime(i):
            answer += 1
    return answer

# 배열에서 m개 골라 순열 만들기 -> 순열 만드는 것 정도는 자주 쓸거같아서 익숙하게 만들어두면 좋을 듯 합니다
def permutation(arr, m):
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
            dfs(depth + 1)
            path.pop()
            used[i] = False

    dfs(0)
    return result


# 소수인지 확인하는 함수
def is_it_prime(num):
    prime = True

    # 2는 무조건 소수
    if num == 1 or num == 0:
        return False
    if num == 2:
        return True

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            prime = False
            break

    return prime

