import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, request
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
def home():
    return render_template("index.html")

@app.route("/map_viz.html")
def mappage():

    return render_template("map_viz.html")

@app.route("/airbnb_listings.geojson")
def getgeojson():
    with open("static/data/airbnb_listings.txt", "r", encoding='utf-8') as f:
        geojson_string = f.read()
    return geojson_string

@app.route("/Vis2.html")
def barGraph():
#  Create our session (link) from Python to the DB
    session = Session(engine)
    # # Query all airbnb
    results_bar = session.query(airbnb.neighbourhood_group, airbnb.neighbourhood, airbnb.room_type, airbnb.price, airbnb.latitude, airbnb.longitude,airbnb.number_of_reviews).all()
    session.close()
    # Create a dictionary from the row data and append to a list of all_airbnbs  
    all_listings = []
    for borough, neighborhood, roomType, price, latitude, longitude, numReviews in results_bar:
        airbnb_dict = {}
        airbnb_dict["neighborhood_group"] = borough
        airbnb_dict["neighborhood"] = neighborhood
        airbnb_dict["room_type"] = roomType
        airbnb_dict["price"] = price
        airbnb_dict["latitude"] = latitude
        airbnb_dict["longitude"] = longitude
        airbnb_dict["number_of_reviews"] = numReviews
        all_listings.append(airbnb_dict)
    return render_template("Vis2.html", data=json.dumps(all_listings, default = myconverter))

# @app.route("/bubble")
# def bubblepage():
# #  Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of airbnb data including specific columns"""
#     # Query all airbnb
#     results_zoomTree = session.query(airbnb.neighbourhood_group, airbnb.neighbourhood, airbnb.latitude, airbnb.longitude, airbnb.room_type, airbnb.price, airbnb.minimum_nights, airbnb.number_of_reviews, airbnb.availability_365).all()
#     session.close()

#     # Create a dictionary from the row data and append to a list of all_airbnbs    
#     return render_template("Vis3.html", data=json.dumps(results_zoomTree, default = myconverter))

@app.route("/Vis3.html")
def zoomTree():
#  Create our session (link) from Python to the DB
    session = Session(engine)
    # """Return a list of airbnb data including all columns"""
    # # Query all airbnb
    results_zoomTree = session.query(airbnb.neighbourhood_group, airbnb.neighbourhood, airbnb.room_type, airbnb.price, airbnb.latitude, airbnb.longitude, airbnb.entry_id, airbnb.name).all()
    session.close()
    # Create a dictionary from the row data and append to a list of all_airbnbs  
    all_listings = []
    for borough, neighborhood, roomType, price, latitude, longitude, entry_id, name in results_zoomTree:
        airbnb_dict = {}
        airbnb_dict["neighborhood_group"] = borough
        airbnb_dict["neighborhood"] = neighborhood
        airbnb_dict["room_type"] = roomType
        airbnb_dict["price"] = price
        airbnb_dict["latitude"] = latitude
        airbnb_dict["longitude"] = longitude
        airbnb_dict["entry_id"] = entry_id
        airbnb_dict["name"] = name
        all_listings.append(airbnb_dict)
    return render_template("Vis3.html", data=json.dumps(all_listings, default = myconverter))



if __name__ == '__main__':
    app.run(debug=True)
