SELECT
    actual_payment_method,
    COUNT(*) AS payments,
    SUM(amount) AS revenue
FROM fact_trip
GROUP BY actual_payment_method
ORDER BY revenue DESC;