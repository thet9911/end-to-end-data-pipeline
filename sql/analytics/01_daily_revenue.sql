SELECT
    DATE(booking_time) AS trip_date,
    SUM(amount) AS revenue,
    COUNT(*) AS total_trips
FROM fact_trip
GROUP BY DATE(booking_time)
ORDER BY trip_date;