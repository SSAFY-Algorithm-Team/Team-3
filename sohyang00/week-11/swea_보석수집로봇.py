# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZwmBfua3q3HBIT3&categoryId=AZwmBfua3q3HBIT3&categoryType=CODE&&&
import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())

dr = [0,1,0,-1]
dc = [1,0,-1,0]

# 이동하는 함수 
def move(r,c,d,target):
    nr = r + dr[d]
    nc = c + dc[d]
    #어떻게 하라는 거임...
    #그래서 몇 번 회전 해야할지 

def find_way():
    


for testCase in range(1, T+1):
    n = int(input())
    grid = [list(map(int,input().split())) for _ in range(n)]
    positions = {}
    for r in range(n):
        for c in range(n):
            if grid[r][c] > 0:
                positions[grid[r][c]] = (r,c)



    

