import numpy as np
import csv
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask import render_template

import json
import datetime

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

#################################################
# Database Setup
#################################################
connection_string = "postgres:Airbnb123@database-1.cs2n53kye3v5.us-west-1.rds.amazonaws.com:5432/airbnb_ny"
engine = create_engine(f'postgresql://{connection_string}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
airbnb = Base.classes.airbnb_db


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
#  Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of airbnb data including all columns"""
    # Query all airbnb
    results = session.query(airbnb.entry_id, airbnb.name, airbnb.host_id, airbnb.neighbourhood_group, airbnb.neighbourhood, airbnb.latitude, airbnb.longitude, airbnb.room_type, airbnb.price, airbnb.minimum_nights, airbnb.number_of_reviews, airbnb.last_review, airbnb.reviews_per_month, airbnb.calculated_host_listings_count, airbnb.availability_365).all()
    session.close()

    # Create a dictionary from the row data and append to a list of all_airbnbs    
    return render_template("index.html", data=json.dumps(results, default = myconverter))

@app.route("/zoomTree")
def zoomTree():
#  Create our session (link) from Python to the DB
    session = Session(engine)

    # """Return a list of airbnb data including all columns"""
    # # Query all airbnb
    results_zoomTree = session.query(airbnb.neighbourhood_group, airbnb.neighbourhood, airbnb.room_type, airbnb.price, airbnb.latitude, airbnb.longitude).all()
    session.close()

    # Create a dictionary from the row data and append to a list of all_airbnbs  

    all_listings = []
    for borough, neighborhood, roomType, price, latitude, longitude in results_zoomTree:
        airbnb_dict = {}
        airbnb_dict["neighborhood_group"] = borough
        airbnb_dict["neighborhood"] = neighborhood
        airbnb_dict["room_type"] = roomType
        airbnb_dict["price"] = price
        airbnb_dict["latitude"] = latitude
        airbnb_dict["longitude"] = longitude
        all_listings.append(airbnb_dict)

    return render_template("test.html", data=json.dumps(all_listings, default = myconverter))

    # with open('Resources/airbnb_df_clean.csv', "r", encoding="utf-8") as csv_file:
    #     data = csv.reader(csv_file, delimiter=',')
    #     first_line = True
    #     listings = []
    #     for row in data:
    #         if not first_line:
    #             listings.append({
    #             "entry_id": row[0],
    #             "host_id": row[2],
    #             "neighborhood_group": row[3],
    #             "neighborhood": row[4],
    #             "latitude": row[5],
    #             "longitude": row[6],
    #             "room_type": row[7],
    #             "price": row[8],
    #             "minimum_nights": row[9],
    #             "number_of_reviews": row[10],
    #             "reviews_per_month": row[12],
    #             "calculated_host_listings_count": row[13],
    #             "availability_365": row[14]
    #             })
    #         else:
    #             first_line = False
    # return render_template("test.html", listings=listings)

if __name__ == '__main__':
    app.run(debug=True)