-- 기출 6. 달러 거래 손익 (SQL)
-- 소요시간: 분 / 시도: 회
-- ※ 이 풀이는 직접 작성하지 않았고, AI(Claude)가 작성한 코드입니다.

-- 거래는 항상 100달러 단위이고 FIFO로 매칭하므로,
-- 사용자별 k번째 SELL은 항상 k번째 BUY와 짝이 된다.
-- → BUY, SELL에 각각 순번을 매기고 같은 순번끼리 JOIN 하면 된다.
WITH BUYS AS (
    SELECT USER_ID,
           RATE,
           ROW_NUMBER() OVER (PARTITION BY USER_ID ORDER BY TRADE_SEQ) AS RN
    FROM USD_TABLES
    WHERE TRADE_TYPE = 'BUY'
),
SELLS AS (
    SELECT USER_ID,
           RATE,
           ROW_NUMBER() OVER (PARTITION BY USER_ID ORDER BY TRADE_SEQ) AS RN
    FROM USD_TABLES
    WHERE TRADE_TYPE = 'SELL'
),
MATCHED AS (
    -- 매도 한 건당 손익
    SELECT S.USER_ID,
           (S.RATE - B.RATE) * 100 AS PNL
    FROM SELLS S
    JOIN BUYS B
      ON S.USER_ID = B.USER_ID
     AND S.RN = B.RN
)
-- 매도가 없는 사용자도 포함하기 위해 전체 사용자 기준으로 LEFT JOIN
SELECT U.USER_ID,
       COALESCE(SUM(M.PNL), 0) AS PROFIT,
       COUNT(CASE WHEN M.PNL > 0 THEN 1 END) AS PROFIT_COUNT
FROM (SELECT DISTINCT USER_ID FROM USD_TABLES) U
LEFT JOIN MATCHED M
  ON U.USER_ID = M.USER_ID
GROUP BY U.USER_ID
ORDER BY U.USER_ID DESC;
