# sql lv1.  강원도에 위치한 생산공장 목록 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/131112
# 소요시간: 15분 / 시도: 2회

SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE LEFT(ADDRESS,3) = '강원도'
ORDER BY FACTORY_ID