-- Creation of external table from parquet green taxi dataset
CREATE OR REPLACE EXTERNAL TABLE `dataengineeringcourse-0001.ny_green_taxi.green_tripdata_2022`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://green_tripdata_2022/*.parquet']
);

-- Creation of non-partitioned table from green taxi external table
CREATE OR REPLACE TABLE dataengineeringcourse-0001.ny_green_taxi.green_tripdata_2022_non_partitioned AS
SELECT * FROM dataengineeringcourse-0001.ny_green_taxi.green_tripdata_2022;

-- Checking external table
SELECT * FROM dataengineeringcourse-0001.ny_green_taxi.green_tripdata_2022 limit 10;

-- Checking non-partitioned table
SELECT * FROM dataengineeringcourse-0001.ny_green_taxi.green_tripdata_2022_non_partitioned limit 10;

-- Counting number of records in green taxi table
SELECT COUNT(*) AS num_records
FROM dataengineeringcourse-0001.ny_green_taxi.green_tripdata_2022;

-- Queries for estimating amount of data in the external and non-pertitioned tables
SELECT COUNT(DISTINCT PULocationID) AS cantidad_distinct_PULocationIDs
FROM dataengineeringcourse-0001.ny_green_taxi.green_tripdata_2022;

SELECT COUNT(DISTINCT PULocationID) AS cantidad_distinct_PULocationIDs
FROM dataengineeringcourse-0001.ny_green_taxi.green_tripdata_2022_non_partitioned;

-- Counting amound records with a fare_amount of 0 
SELECT COUNT(*) AS num_records_with_fare_0
FROM dataengineeringcourse-0001.ny_green_taxi.green_tripdata_2022
WHERE fare_amount = 0;

-- Query for calculate the size in MB of tables
SELECT
  table_id AS tabla,
  row_count AS num_records,
  size_bytes / (1024 * 1024) AS size_total_mb
FROM
  `dataengineeringcourse-0001.ny_green_taxi.__TABLES__`;