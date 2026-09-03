-- 프로그래머스 Lv1. 과일로 만든 아이스크림 고르기
-- https://school.programmers.co.kr/learn/courses/30/lessons/133025

SELECT FH.FLAVOR
FROM FIRST_HALF AS FH
JOIN ICECREAM_INFO AS II
ON FH.FLAVOR = II.FLAVOR
WHERE FH.TOTAL_ORDER > 3000
AND II.INGREDIENT_TYPE = 'fruit_based'
ORDER BY FH.TOTAL_ORDER DESC;
