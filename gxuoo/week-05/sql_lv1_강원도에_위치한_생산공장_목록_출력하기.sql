-- 프로그래머스 SQL Lv1. 강원도에 위치한 생산공장 목록 출력하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131112
-- 소요시간: 1분 / 시도: 1회

-- 코드를 입력하세요
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS FROM FOOD_FACTORY
    WHERE ADDRESS LIKE '강원도%'
    ORDER BY FACTORY_ID;
