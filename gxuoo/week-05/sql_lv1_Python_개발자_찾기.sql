-- 프로그래머스 SQL Lv1. Python 개발자 찾기
-- https://school.programmers.co.kr/learn/courses/30/lessons/276013
-- 소요시간: 3분 / 시도: 1회

-- 코드를 작성해주세요
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME FROM DEVELOPER_INFOS
    WHERE SKILL_1 = 'Python' OR SKILL_2 = 'Python' OR SKILL_3 = 'Python'
    ORDER BY ID;
