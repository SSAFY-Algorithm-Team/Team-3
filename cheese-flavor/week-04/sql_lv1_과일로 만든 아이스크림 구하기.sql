# sql lv1. 과일로 만든 아이스크림 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/133025
# 소요시간: 10분 / 시도: 2회

SELECT A.FLAVOR   #무조건 어디 위치인지를 밝혀야하네?
From FIRST_HALF AS A JOIN ICECREAM_INFO AS B ON A.FLAVOR = B.FLAVOR
WHERE A.TOTAL_ORDER >= 3000 AND B.INGREDIENT_TYPE = 'fruit_based'
ORDER BY FLAVOR ASC