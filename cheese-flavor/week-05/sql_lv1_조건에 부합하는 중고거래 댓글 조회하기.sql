# sql lv1.  조건에 부합하는 중고거래 댓글 조회하기
# https://school.programmers.co.kr/learn/courses/30/lessons/164673
# 소요시간: 15분 / 시도: 1회


# 조인 구문을 가끔 까먹네
SELECT A.TITLE, A.BOARD_ID, B.REPLY_ID, B.WRITER_ID, B.CONTENTS, B.CREATED_DATE
FROM USED_GOODS_BOARD AS A JOIN USED_GOODS_REPLY AS B ON A.BOARD_ID = B.BOARD_ID
WHERE LEFT(B.CREATED_DATE,7) = '2022-10'
ORDER BY B.CREATED_DATE ASC, A.TITLE ASC