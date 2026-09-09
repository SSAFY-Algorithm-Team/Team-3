# sql lv1.  조건에 맞는 도서 리스트 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/144853
# 소요시간: 5분 / 시도: 1회

SELECT BOOK_ID, PUBLISHED_DATE
FROM BOOK
WHERE PUBLISHED_DATE >= '2021-01-01' AND PUBLISHED_DATE <= '2021-12-31' AND CATEGORY = '인문'
ORDER BY PUBLISHED_DATE