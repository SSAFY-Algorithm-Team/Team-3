# sql lv1. 아픈 동물 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/59036
# 소요시간: 3분 / 시도: 1회

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID