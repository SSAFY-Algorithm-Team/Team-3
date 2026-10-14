-- 프로그래머스 SQL Lv2. 연도별 대장균 크기의 편차 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/299310
-- 소요시간: 10분 / 시도: 3회

SELECT
    YEAR(DIFFERENTIATION_DATE) AS YEAR,
    MAX(SIZE_OF_COLONY) OVER(
        PARTITION BY YEAR(DIFFERENTIATION_DATE)
    ) - SIZE_OF_COLONY AS YEAR_DEV,
    ID
FROM ECOLI_DATA
ORDER BY YEAR ASC, YEAR_DEV ASC;
