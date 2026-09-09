-- 프로그래머스 SQL Lv1. 조건에 부합하는 중고거래 댓글 조회하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/164673
-- 소요시간: 8분 / 시도: 4회

-- 코드를 입력하세요
SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
    FROM USED_GOODS_BOARD B JOIN USED_GOODS_REPLY R ON B.BOARD_ID = R.BOARD_ID
    WHERE YEAR(B.CREATED_DATE) = 2022 AND MONTH(B.CREATED_DATE) = 10
    ORDER BY R.CREATED_DATE, B.TITLE;
