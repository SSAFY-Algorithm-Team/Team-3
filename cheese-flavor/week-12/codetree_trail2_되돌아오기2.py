# Day 02 | 2026-11-12
# 코드트리 Trail 2 | Chapter 05: dx dy technique | Lesson 03: dx dy technique
# Problem: 되돌아오기 2
# URL: https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-come-back-2/description
# 소요시간: 20분 / 시도: 2회

commands = input()

# Please write your code here.
# F는 직진, R 오른쪽, L 왼쪽

mv = [-1, 0, 0, 1, 1, 0, 0, -1]
time = 0
c, r, d = 0, 0, 0
possible = False

for command in commands:
    if command == 'F':
        c += mv[d]
        r += mv[d+1]
        time += 1

        if c == 0 and r == 0:
            print(time)
            possible = True
            break

    elif command == 'R':
        d = (d+2)%8
        time += 1

    elif command == 'L':
        d = (d-2)%8
        time += 1

# 출력안되면 -1
if not possible:
    print(-1)

            
            
            
        
    


