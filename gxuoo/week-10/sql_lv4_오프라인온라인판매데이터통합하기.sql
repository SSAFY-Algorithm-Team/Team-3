-- 프로그래머스 SQL Lv4. 오프라인/온라인 판매 데이터 통합하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131537
-- 소요시간: 분 / 시도: 회

'''
SELECT 
    n.SALES_DATE, 
    n.PRODUCT_ID, 
    NULL AS USER_ID,
    n.SALES_AMOUNT
FROM ONLINE_SALE n JOIN OFFLINE_SALE f
    ON n.PRODUCT_ID = f.PRODUCT_ID
WHERE YEAR(n.SALES_DATE) = 2022
  AND MONTH(n.SALES_DATE) = 3
ORDER BY n.SALES_DATE, n.PRODUCT_ID, USER_ID ASC;

여기까지 작성했는데,,, 흠 UNION ALL을 써야 된다고 하네요,,,
나는 감자다.... JOIN을 사용하면 일부 데이터가 사라지니, UNION ALL을 사용해서 모든 데이터를 합친다.
'''

SELECT
    n.SALES_DATE,
    n.PRODUCT_ID,
    n.USER_ID,
    n.SALES_AMOUNT
FROM ONLINE_SALE n
WHERE YEAR(n.SALES_DATE) = 2022
  AND MONTH(n.SALES_DATE) = 3

UNION ALL

SELECT
    f.SALES_DATE,
    f.PRODUCT_ID,
    NULL AS USER_ID,
    f.SALES_AMOUNT
FROM OFFLINE_SALE f
WHERE YEAR(f.SALES_DATE) = 2022
  AND MONTH(f.SALES_DATE) = 3

ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;
