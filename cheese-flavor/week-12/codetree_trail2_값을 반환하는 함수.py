# Day 01 | 2026-11-11
# 코드트리 Trail 2 | Chapter 01: 함수 | Lesson 02: 값을 반환하는 함수
# Problem: 그 계절, 그 날
# URL: https://www.codetree.ai/ko/trails/complete/curated-cards/test-that-season-that-day/description
# 소요시간: 15분 / 시도: 2회

Y, M, D = map(int, input().split())

# Please write your code here.
def year(y):
    if y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return True
    if y % 4 == 0 and y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    return False
    
def season(m):
    if 3 <= m <= 5:
        return 'Spring'
    elif 6 <= m <= 8:
        return 'Summer'
    elif 9 <= m <= 11:
        return 'Fall'
    return 'Winter'

def check(y, m, d):
    year1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year(y):
        if year2[m-1] >= d:
            return season(m)
    else:
        if year1[m-1] >= d:
            return season(m)

    return -1

print(check(Y, M, D))
            
            
            
        
    


