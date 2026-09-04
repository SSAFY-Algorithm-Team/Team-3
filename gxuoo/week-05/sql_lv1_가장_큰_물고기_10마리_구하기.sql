-- 프로그래머스 SQL Lv1. 가장 큰 물고기 10마리 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/298517
-- 소요시간: 1분 / 시도: 1회

-- 코드를 작성해주세요
SELECT ID, LENGTH FROM FISH_INFO
    WHERE LENGTH > 10
    ORDER BY LENGTH DESC, ID LIMIT 10;
