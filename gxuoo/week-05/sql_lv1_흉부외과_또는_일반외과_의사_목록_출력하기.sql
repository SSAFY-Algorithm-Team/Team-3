-- 프로그래머스 SQL Lv1. 흉부외과 또는 일반외과 의사 목록 출력하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/132203
-- 소요시간: 6분 / 시도: 1회

-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, HIRE_YMD FROM DOCTOR
    WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
    ORDER BY HIRE_YMD DESC, DR_NAME ASC;
