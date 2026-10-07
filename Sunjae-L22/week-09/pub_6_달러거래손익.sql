# 달러거래손익
# 소요시간 : 모르겠어요 GPT씀

WITH ranked AS (
    SELECT
        USER_ID,
        TRADE_TYPE,
        RATE,
        ROW_NUMBER() OVER (
            PARTITION BY USER_ID, TRADE_TYPE
            ORDER BY TRADE_SEQ
        ) AS RN
    FROM USD_TABLES
),
profits AS (
    SELECT
        s.USER_ID,
        (s.RATE - b.RATE) * 100 AS PROFIT
    FROM ranked s
    JOIN ranked b
        ON s.USER_ID = b.USER_ID
        AND s.RN = b.RN
        AND b.TRADE_TYPE = 'BUY'
    WHERE s.TRADE_TYPE = 'SELL'
)
SELECT
    u.USER_ID,
    COALESCE(SUM(p.PROFIT), 0) AS PROFIT,
    SUM(
        CASE WHEN p.PROFIT > 0 THEN 1 ELSE 0 END
    ) AS PROFIT_COUNT
FROM (
    SELECT DISTINCT USER_ID
    FROM USD_TABLES
) u
LEFT JOIN profits p
    ON u.USER_ID = p.USER_ID
GROUP BY u.USER_ID
ORDER BY u.USER_ID DESC;