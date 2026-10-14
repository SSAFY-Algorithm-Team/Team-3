-- 프로그래머스 SQL Lv4. 입양 시각 구하기(2)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59413
-- 소요시간: 40분 / 시도: 3회

'''
SELECT 
    HOUR(DATETIME) AS HOUR,    
    COUNT(*) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR(DATETIME)
ORDER BY HOUR;

여기서 막힘...
시간이 없는 걸 어떻게 생성하는지 몰라서 GPT 물어봄..

WITH RECURSIVE 이름 AS (
    -- 1. 시작값
    SELECT 0 AS N

    UNION ALL

    -- 2. 반복할 내용
    SELECT N + 1
    FROM 이름
    WHERE N < 5
)
SELECT * FROM 이름;
'''

WITH RECURSIVE HOURS AS (
    SELECT 0 AS HR
    UNION ALL
    SELECT HR + 1
    FROM HOURS
    WHERE HR < 23
)
SELECT
    H.HR AS HOUR,
    COUNT(A.ANIMAL_ID) AS COUNT
FROM HOURS H
LEFT JOIN ANIMAL_OUTS A
    ON H.HR = HOUR(A.DATETIME)
GROUP BY H.HR
ORDER BY H.HR;
