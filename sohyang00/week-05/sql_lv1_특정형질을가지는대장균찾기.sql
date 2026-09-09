-- 프로그래머스 Lv1. 특정 형질을 가지는 대장균 찾기
-- https://school.programmers.co.kr/learn/courses/30/lessons/301646

SELECT COUNT(ID) AS COUNT
FROM ECOLI_DATA
WHERE GENOTYPE & 2 = 0 AND (GENOTYPE & 1 > 0 OR GENOTYPE & 4 > 0)
# 형질 번호는 비트 위치라서 2^(형질번호-1)
# 3번 형질 = (0100) 4, 4번 형질 = (1000) 8
