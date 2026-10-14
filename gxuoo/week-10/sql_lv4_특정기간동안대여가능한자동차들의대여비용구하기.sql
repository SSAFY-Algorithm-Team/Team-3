-- 프로그래머스 SQL Lv4. 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/157339
-- 소요시간: 30분 / 시도: 5회

'''
자동차 종류: 세단, SUV
대여기간: 22년 11월 1일부터 30일
대여금액: 50만원 이상 200만원 미만

JOIN을 얼마나 해야되는지 헷갈렸고, 11월 계산을 잘못했는데 GPT한테 2번 물어보고 풀엇음..
'''

SELECT 
    c.CAR_ID AS CAR_ID,
    c.CAR_TYPE AS CAR_TYPE,
    FLOOR(c.DAILY_FEE * 30 * (1 - p.DISCOUNT_RATE / 100)) AS FEE
FROM CAR_RENTAL_COMPANY_CAR c 
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
    ON c.CAR_TYPE = p.CAR_TYPE
    AND p.DURATION_TYPE = '30일 이상'
WHERE (c.CAR_TYPE = '세단' or c.CAR_TYPE = 'SUV')
    AND c.CAR_ID NOT IN (
        SELECT CAR_ID 
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE <= '2022-11-30'
            AND END_DATE >= '2022-11-01'
    )
HAVING FEE >= 500000 AND FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC;
