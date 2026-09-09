-- 프로그래머스 SQL Lv1. 여러 기준으로 정렬하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/59404
-- 소요시간: 2분 / 시도: 1회

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS
    ORDER BY NAME, DATETIME DESC;
