SELECT
    driver_id,
    COUNT(*) AS trips,
    SUM(amount) AS revenue,
    AVG(rating) AS avg_rating
FROM fact_trip
GROUP BY driver_id
ORDER BY revenue DESC;