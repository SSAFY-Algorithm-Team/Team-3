-- 프로그래머스 SQL Lv1. 어린 동물 찾기
-- https://school.programmers.co.kr/learn/courses/30/lessons/59037
-- 소요시간: 1분 / 시도: 1회

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
    WHERE INTAKE_CONDITION != 'Aged';
