SELECT
    HOUR(booking_time) AS booking_hour,
    COUNT(*) AS trips
FROM fact_trip
GROUP BY HOUR(booking_time)
ORDER BY booking_hour;