# Day 01 | 2026-11-11
# 코드트리 Trail 1 | Chapter 08: 2차원 배열 | Lesson 02: 새로운 2차원 배열의 선언
# Problem: 두 개의 격자 비교하기
# URL: https://www.codetree.ai/ko/trails/complete/curated-cards/test-compare-two-grid/description
# 소요시간: 8분 / 시도: 1회

n, m = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            print(0, end = ' ')
        else:
            print(1, end = ' ')
    print()

            
            
            
        
    


