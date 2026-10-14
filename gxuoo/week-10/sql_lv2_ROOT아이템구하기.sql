-- 프로그래머스 SQL Lv2. ROOT 아이템 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/273710
-- 소요시간: 10분 / 시도: 1회

SELECT I.ITEM_ID, ITEM_NAME
FROM ITEM_INFO I
JOIN ITEM_TREE T
    ON I.ITEM_ID = T.ITEM_ID
WHERE T.PARENT_ITEM_ID IS NULL
ORDER BY I.ITEM_ID;
