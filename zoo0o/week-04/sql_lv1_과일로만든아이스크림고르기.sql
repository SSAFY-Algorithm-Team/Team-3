# 프로그래머스 SQL Lv1. 과일로 만든 아이스크림 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/133025

SELECT FLAVOR
FROM FIRST_HALF
WHERE TOTAL_ORDER > 3000
  AND FLAVOR IN (
      SELECT FLAVOR
      FROM ICECREAM_INFO
      WHERE INGREDIENT_TYPE = 'fruit_based'
  )
ORDER BY TOTAL_ORDER DESC;