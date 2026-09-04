# 프로그래머스 Lv2. 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 소요시간: 30분 / 시도: 4회


def solution(phone_book):
    #해시 형태를 고려해보자
    '''
    hash_map이 set이면 → 해시 테이블 조회라서 O(1) -> 이게 더 빠르군
    hash_map이 지금처럼 list이면 → 리스트를 처음부터 끝까지 하나씩 비교하는 O(n)
    '''
    hash_map = set(phone_book)
    length = set()
    
    for i in phone_book:
        length.add(len(i))
    
    
    for number in phone_book:
        for l in length:
            if l >= len(number):
                continue
            else:
                if number[:l] in hash_map:
                    return False      

        
    return True  # set은 혼자 출력하면 안되고 반드시 list로 묶어서
    
    
''' 1. 코드는 맞았으나 효율성 문제 -> 너무 어렵게 풀려고 생각한듯

def solution(phone_book):
    answer = True
    l = len(phone_book)

    for i in range(l):
        for j in range(i+1, l):
            if len(phone_book[i]) <= len(phone_book[j]):
                if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                    return False
                
            elif len(phone_book[i]) > len(phone_book[j]):
                if phone_book[j] == phone_book[i][:len(phone_book[j])]:
                    return False
                    
    return answer
'''

'''2번 - 인접성을 고려함

def solution(phone_book):
    l = len(phone_book)
    phone_book.sort()
    
    for i in range(l-1):
        a, b = phone_book[i], phone_book[i+1]
        if a == b[:len(a)]:
            return False
        
    return True
'''

'''3번 - 인접성을 startswith 함수로 활용

def solution(phone_book):
    l = len(phone_book)
    phone_book.sort()
    
    for i in range(l-1):
        a, b = phone_book[i], phone_book[i+1]
        if b.startswith(a):
            return False
        
    return True
'''