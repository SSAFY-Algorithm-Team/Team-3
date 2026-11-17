# Day 02 | 2026-11-12
# 코드트리 Trail 2 | Chapter 05: dx dy technique | Lesson 03: dx dy technique
# Problem: 되돌아오기 
# URL: https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-come-back/description
# 소요시간: 20분 / 시도: 1회


N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
c, r = 0, 0
sum_dist = 0
possible = False

# 그냥 반복문 기반
for i in range(N):
    if not possible:

        if dir[i] == 'W':
            for _ in range(1, dist[i]+1):
                r -= 1
                sum_dist += 1

                if c == 0 and r == 0:
                    print(sum_dist)
                    possible = True
                    break

        elif dir[i] == 'E':
            for _ in range(1, dist[i]+1):
                r += 1
                sum_dist += 1

                if c == 0 and r == 0:
                    print(sum_dist)
                    possible = True
                    break

        elif dir[i] == 'S':
            for _ in range(1, dist[i]+1):
                c += 1
                sum_dist += 1

                if c == 0 and r == 0:
                    print(sum_dist)
                    possible = True
                    break

        else:
            for _ in range(1, dist[i]+1):
                c -= 1
                sum_dist += 1

                if c == 0 and r == 0:
                    print(sum_dist)
                    possible = True
                    break

if not possible:
    print(-1)

            
            
            
        
    


