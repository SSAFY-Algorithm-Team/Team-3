N = int(input())
T = int(input())
score = []
teams= [0 for _ in range(T)]

for _ in range(N):
    t, s = map(int, input().split())
    score.append([t, s])

for s in score:
    teams[s[0]-1] += s[1]

result = max(teams) - min(teams)
print(result)