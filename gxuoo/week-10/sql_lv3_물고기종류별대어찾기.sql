-- 프로그래머스 SQL Lv3. 물고기 종류 별 대어 찾기
-- https://school.programmers.co.kr/learn/courses/30/lessons/293261
-- 소요시간: 35분 / 시도: 3회

SELECT F.ID, N.FISH_NAME, F.LENGTH
    FROM FISH_INFO F
    JOIN FISH_NAME_INFO N ON F.FISH_TYPE = N.FISH_TYPE
    WHERE (F.FISH_TYPE, F.LENGTH) IN (
        SELECT FISH_TYPE, MAX(LENGTH)
        FROM FISH_INFO
        GROUP BY FISH_TYPE
    )
    ORDER BY F.ID;
