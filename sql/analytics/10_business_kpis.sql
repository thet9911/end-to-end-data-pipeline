SELECT
    COUNT(*) AS total_trips,
    COUNT(DISTINCT customer_id) AS total_customers,
    COUNT(DISTINCT driver_id) AS total_drivers,
    SUM(amount) AS total_revenue,
    AVG(amount) AS average_fare,
    AVG(distance_km) AS average_distance,
    AVG(duration_min) AS average_duration,
    AVG(rating) AS average_rating
FROM fact_trip;