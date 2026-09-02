# 프로그래머스 Lv1. 인기있는아이스크림
# https://school.programmers.co.kr/learn/courses/30/lessons/133024
# 소요시간: 5분 / 시도: 1회

SELECT FLAVOR FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC;