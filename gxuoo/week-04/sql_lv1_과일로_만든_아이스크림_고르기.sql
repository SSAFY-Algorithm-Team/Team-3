-- 프로그래머스 SQL Lv1. 과일로 만든 아이스크림 고르기
-- https://school.programmers.co.kr/learn/courses/30/lessons/133025
-- 소요시간: 30분 / 시도: 3회

SELECT F.FLAVOR AS FLAVOR
  FROM FIRST_HALF F
  JOIN ICECREAM_INFO I ON F.FLAVOR = I.FLAVOR
  WHERE F.TOTAL_ORDER > 3000 AND I.INGREDIENT_TYPE = 'fruit_based'
  ORDER BY F.TOTAL_ORDER DESC;
