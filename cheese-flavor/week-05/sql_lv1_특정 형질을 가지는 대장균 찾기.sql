# sql lv1.  특정 형질을 가지는 대장균 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/301646
# 소요시간: 20분 / 시도: 4회

SELECT COUNT(GENOTYPE)
FROM ECOLI_DATA

#놀랍게도 BIT 연산자 까먹어서 별에별짓을 다함
WHERE (GENOTYPE & 2) = 0
  AND ((GENOTYPE & 1) != 0 OR (GENOTYPE & 4) != 0)

#LPAD 자리수에 맞게 숫자 또는 문자를 추가하는 함수
#BIN = BIT로 바꿔주는 함수
#SUBSTRING = 시작부터 길이만큼 짜르는 함수

'''
SELECT COUNT(GENOTYPE)
FROM ECOLI_DATA
WHERE SUBSTRING(LPAD(BIN(GENOTYPE),3,'0'),2,1) = 0 AND 
(SUBSTRING(LPAD(BIN(GENOTYPE),3,'0'),1,1) = 1 OR 
SUBSTRING(LPAD(BIN(GENOTYPE),3,'0'),3,1) = 1)
'''