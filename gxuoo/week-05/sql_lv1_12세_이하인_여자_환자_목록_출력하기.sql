-- 프로그래머스 SQL Lv1. 12세 이하인 여자 환자 목록 출력하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/132201
-- 소요시간: 6분 / 시도: 3회

-- 코드를 입력하세요
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO FROM PATIENT
    WHERE AGE <= 12 AND GEND_CD = 'W'
    ORDER BY AGE DESC, PT_NAME ASC;
