# 기출 5: 결제 실패 조회
# 소요시간: 15분 / 시도: 2회


#EXISTS 체험기 / select 1을 처음 경험

SELECT p.PAYMNET_ID
FROM PAYMENT p
WHERE NOT EXISTS(
    SELECT 1       # 조건에 맞는 행마다 1을 반환
    FROM PAYMENT_ATTEMPTS a
    WHERE a.PAYMNET_ID = p.PAYMNET_ID
        AND a.PAYMNET_DATE <= p.SCHEDULED_DATE
        AND a.STATUS = 'SUCCESS'
)
ORDER BY p.PAYMNET_ID DESC;