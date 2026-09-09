-- 프로그래머스 SQL Lv1. 특정 형질을 가지는 대장균 찾기
-- https://school.programmers.co.kr/learn/courses/30/lessons/301646
-- 소요시간: 7분 / 시도: 1회

-- 코드를 작성해주세요
SELECT COUNT(*) AS COUNT FROM ECOLI_DATA
    WHERE GENOTYPE & 2 = 0
    AND GENOTYPE & 5 > 0;
