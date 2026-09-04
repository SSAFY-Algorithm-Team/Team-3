# 프로그래머스 Lv1. 과일로만든아이스크림고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/133025
# 소요시간: 10분 / 시도: 1회

SELECT F.FLAVOR
FROM FIRST_HALF F
JOIN ICECREAM_INFO I ON F.FLAVOR = I.FLAVOR
WHERE F.TOTAL_ORDER > 3000
  AND I.INGREDIENT_TYPE = 'fruit_based'
ORDER BY F.TOTAL_ORDER DESC;