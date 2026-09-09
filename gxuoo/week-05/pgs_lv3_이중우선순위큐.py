# 프로그래머스 Lv3. 이중우선순위큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# 소요시간: 40분 / 시도: 2회

# 첫 번째 풀이 (힙 사용 X, 근데 아마 테케 이슈로 정답인 듯)
def solution(operations):
    answer = []
    result = []
    
    for op in operations:
        command, num = op.split()
        num = int(num)
        
        if command == 'I':
            answer.append(num)
        else:
            if not len(answer):
                continue
                
            if num == 1:
                answer.remove(max(answer))
            else:
                answer.remove(min(answer))
    
    if len(answer):
        result.append(max(answer))
        result.append(min(answer))
    else:
        result.append(0)
        result.append(0)
        
    return result


# 두 번재 풀이 -> AI가 짜준 코드인데 이해가 잘 안 간다...
import heapq

def solution(operations):
    # heapq는 최소 힙만 제공하므로, 부호를 뒤집은 값을 담는 힙을 하나 더 둔다.
    min_heap = []
    max_heap = []

    # alive[i]: i번째 연산으로 삽입된 원소가 아직 큐에 살아있는가.
    alive = [False] * len(operations)

    # 실제로 살아있는 원소의 개수.
    size = 0

    for i, op in enumerate(operations):
        command, num = op.split()
        num = int(num)

        if command == 'I':
            # 튜플로 넣는 이유:
            #   1) 값이 중복돼도 인덱스 i로 개별 원소를 구분할 수 있다.
            #   2) 한쪽 힙에서 pop한 원소가 다른 쪽에서도 같은 원소인지 i로 식별할 수 있다.
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            alive[i] = True
            size += 1

        else:
            # 빈 큐에 대한 삭제 연산은 무시
            if size == 0:
                continue

            if num == 1:
                # ── 최댓값 삭제 ──
                # max_heap의 top이 "이미 min_heap 쪽에서 삭제된 시체"일 수 있다.
                # 살아있는 원소가 나올 때까지 시체를 걷어낸다.
                #
                # 이 while이 무한 루프나 IndexError를 내지 않는 이유:
                # size > 0 이므로 힙 안에 살아있는 원소가 최소 하나는
                # 반드시 존재한다. 즉 언젠가는 조건이 거짓이 된다.
                while not alive[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                _, idx = heapq.heappop(max_heap)
            else:
                # ── 최솟값 삭제 ── (위와 대칭)
                while not alive[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                _, idx = heapq.heappop(min_heap)

            # 지연 삭제의 핵심:
            # 반대편 힙을 뒤져서 실제로 제거하지 않는다. (그러면 O(n))
            # 사망 표시만 남기고, 나중에 그 원소가 top으로 올라왔을 때
            # 위의 while 루프가 알아서 걷어낸다.
            alive[idx] = False
            size -= 1

    if size == 0:
        return [0, 0]

    # 루프가 끝난 시점에도 각 힙의 top이 시체일 수 있다.
    # (반대편에서 삭제됐지만 이쪽에서는 아직 안 걷힌 원소)
    # 답을 읽기 전에 한 번 더 정리해준다.
    while not alive[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while not alive[min_heap[0][1]]:
        heapq.heappop(min_heap)

    # max_heap에는 부호를 뒤집어 넣었으므로 다시 뒤집어서 반환
    return [-max_heap[0][0], min_heap[0][0]]
