SELECT
    driver_id,
    AVG(rating) AS average_rating
FROM fact_trip
GROUP BY driver_id
ORDER BY average_rating DESC;