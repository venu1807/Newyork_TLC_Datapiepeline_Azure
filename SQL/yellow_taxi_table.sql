CREATE TABLE YellowTaxi
(
   
    VendorID int,
    tpep_pickup_datetime datetime,
    tpep_dropoff_datetime datetime,
    passenger_count int,
    trip_distance decimal(3,3),
    RatecodeID	int,
    store_and_fwd_flag	varchar(25),
    PULocationID int,
    DOLocationID int,
    payment_type int,
    fare_amount	decimal(3,3),
    extra decimal(3,3),
    mta_tax decimal(3,3),
    tip_amount decimal(3,3),
    tolls_amount decimal(3,3),
    ehail_fee decimal(3,3),
    improvement_surcharge decimal(3,3),
    total_amount decimal(3,3),
    congestion_surcharge decimal(3,3)
);