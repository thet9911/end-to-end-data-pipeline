SELECT
    customer_id,
    COUNT(*) AS total_trips,
    SUM(amount) AS spending
FROM fact_trip
GROUP BY customer_id
ORDER BY spending DESC
LIMIT 10;