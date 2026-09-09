-- 프로그래머스 SQL Lv1. 조건에 맞는 도서 리스트 출력하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/144853
-- 소요시간: 5분 / 시도: 2회

-- 코드를 입력하세요
SELECT BOOK_ID, PUBLISHED_DATE FROM BOOK
    WHERE CATEGORY = '인문' AND YEAR(PUBLISHED_DATE) = 2021
    ORDER BY PUBLISHED_DATE ASC
