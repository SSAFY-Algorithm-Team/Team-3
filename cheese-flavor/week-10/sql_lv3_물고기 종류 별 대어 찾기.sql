# sql lv3.  물고기 종류 별 대어 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/293261
# 소요시간: 20분 / 시도: 2회

# 과목평가 문제랑 비슷한 친구 / 그때도 틀려서 또 틀림

SELECT f.ID, i.FISH_NAME, f.LENGTH

FROM FISH_INFO f JOIN FISH_NAME_INFO i 
    ON f.FISH_TYPE = i.FISH_TYPE
    
# 동일한 테이블을 다시 쓸경우, 별칭을 다르게 두어서 진행
WHERE f.LENGTH = (
    SELECT MAX(f2.LENGTH)
    FROM FISH_INFO f2
    WHERE f.FISH_TYPE = f2.FISH_TYPE
)

ORDER BY f.ID