CREATE TABLE GreenTaxi
(
   
    VendorID int,
    lpep_pickup_datetime datetime,
    lpep_dropoff_datetime datetime,
    store_and_fwd_flag	varchar(25),
    RatecodeID	int,
    PULocationID int,
    DOLocationID int,
    passenger_count int,
    trip_distance decimal(3,3),
    fare_amount	decimal(3,3),
    extra decimal(3,3),
    mta_tax decimal(3,3),
    tip_amount decimal(3,3),
    tolls_amount decimal(3,3),
    ehail_fee deciamal(3,3),
    improvement_surcharge decimal(3,3),
    total_amount decimal(3,3),
    payment_type int,
    trip_type int,
    congestion_surcharge decimal(3,3)
);
