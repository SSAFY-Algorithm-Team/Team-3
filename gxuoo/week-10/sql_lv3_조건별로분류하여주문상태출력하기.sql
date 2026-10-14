-- 프로그래머스 SQL Lv3. 조건별로 분류하여 주문상태 출력하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131113
-- 소요시간: 5분 / 시도: 1회

SELECT
    ORDER_ID,
    PRODUCT_ID,
    OUT_DATE,
    CASE
        WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
        WHEN OUT_DATE > '2022-05-01' THEN '출고대기'
        ELSE '출고미정'
    END AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID;
