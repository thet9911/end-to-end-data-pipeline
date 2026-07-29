SELECT
    customer_id,
    MIN(DATE(booking_time)) AS first_trip,
    MAX(DATE(booking_time)) AS last_trip,
    COUNT(*) AS total_trips
FROM fact_trip
GROUP BY customer_id;