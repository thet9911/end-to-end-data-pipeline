SELECT
    trip_status,
    COUNT(*) AS trips
FROM fact_trip
GROUP BY trip_status;