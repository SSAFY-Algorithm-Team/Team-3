# 프로그래머스 SQL Lv1. 인기있는 아이스크림
# https://school.programmers.co.kr/learn/courses/30/lessons/151136

SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC;