-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/zu3m3x
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "airbnb_db" (
    "id" serial   NOT NULL,
    "entry_id" int   NOT NULL,
    "name" varchar   NOT NULL,
    "host_id" int   NOT NULL,
    "neighbourhood_group" varchar   NOT NULL,
    "neighbourhood" varchar   NOT NULL,
    "latitude" float8   NOT NULL,
    "longitude" float8   NOT NULL,
    "room_type" varchar   NOT NULL,
    "price" int   NOT NULL,
    "minimum_nights" int   NOT NULL,
    "number_of_reviews" int   NOT NULL,
    "last_review" date   NOT NULL,
    "reviews_per_month" float4   NOT NULL,
    "calculated_host_listings_count" int   NOT NULL,
    "availability_365" int   NOT NULL,
    CONSTRAINT "pk_airbnb_db" PRIMARY KEY (
        "id"
     )
);

