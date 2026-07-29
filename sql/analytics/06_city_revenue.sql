SELECT
    pickup_location,
    SUM(amount) AS revenue
FROM fact_trip
GROUP BY pickup_location
ORDER BY revenue DESC;