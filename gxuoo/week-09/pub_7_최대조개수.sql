-- 기출 7. 최대 조 개수 (SQL)
-- 소요시간: 20분 / 시도: 3회

SELECT MIN(cnt)
FROM (
    SELECT programming_language, COUNT(*) AS cnt
    FROM APPLICANTS
    GROUP BY programming_language
) language_count
