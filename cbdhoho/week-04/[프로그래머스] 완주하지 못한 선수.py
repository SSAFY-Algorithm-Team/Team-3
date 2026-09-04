def solution(participant, completion):
    answer = ''
    done = {}
    for p in participant:
        if p not in done:
            done[p] = 1
        else:
            done[p] += 1
    for c in completion:
        done[c] -= 1
    for d in done:
        if done[d] > 0:
            answer = d
    return answer