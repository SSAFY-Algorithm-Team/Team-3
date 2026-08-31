# sql lv1. 평균 일일 대여 요금 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/151136
# 소요시간: 10분 / 시도: 2회

SELECT ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'