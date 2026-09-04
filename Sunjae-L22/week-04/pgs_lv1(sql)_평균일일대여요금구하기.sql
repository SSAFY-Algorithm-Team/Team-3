# 프로그래머스 Lv1. 평균일일대여요금구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/151136
# 소요시간: 5분 / 시도: 1회

SELECT ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV';