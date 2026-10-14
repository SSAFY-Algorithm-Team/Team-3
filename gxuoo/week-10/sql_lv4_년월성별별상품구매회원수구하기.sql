-- 프로그래머스 SQL Lv4. 년, 월, 성별 별 상품 구매 회원 수 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131532
-- 소요시간: 20분 / 시도: 3회

SELECT
    YEAR(o.SALES_DATE) AS YEAR,
    MONTH(o.SALES_DATE) AS MONTH,
    u.GENDER,
    COUNT(DISTINCT u.USER_ID) AS USERS
FROM USER_INFO u
JOIN ONLINE_SALE o
    ON u.USER_ID = o.USER_ID
WHERE u.GENDER IS NOT NULL
GROUP BY YEAR(o.SALES_DATE), MONTH(o.SALES_DATE), u.GENDER
ORDER BY YEAR, MONTH, GENDER;
