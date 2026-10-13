-- 프로그래머스 SQL Lv3. 대장균의 크기에 따라 분류하기 2
-- https://school.programmers.co.kr/learn/courses/30/lessons/301649
-- 소요시간: 15분 / 시도: 4회

SELECT
    ID,
    CASE
        WHEN ratio <= 0.25 THEN 'CRITICAL'
        WHEN ratio <= 0.50 THEN 'HIGH'
        WHEN ratio <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM (
    SELECT
        ID,
        PERCENT_RANK() OVER (
            ORDER BY SIZE_OF_COLONY DESC
        ) AS ratio
    FROM ECOLI_DATA
) AS ranked
ORDER BY ID;
