import numpy as np

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

    """Return a list of airbnb data including all columns"""
    # Query all airbnb
    results_zoomTree = session.query(airbnb.neighbourhood_group, airbnb.neighbourhood, airbnb.latitude, airbnb.longitude, airbnb.room_type, airbnb.price, airbnb.minimum_nights, airbnb.number_of_reviews, airbnb.availability_365).all()
    session.close()

    # Create a dictionary from the row data and append to a list of all_airbnbs    
    return render_template("test.html", data=json.dumps(results_zoomTree, default = myconverter))


    

    



# @app.route("/api/v1.0/names")
# def names():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#     results = session.query(Passenger.name).all()

#     session.close()

#     # Convert list of tuples into normal list
#     all_names = list(np.ravel(results))

#     return jsonify(all_names)


# @app.route("/api/v1.0/passengers")
# def passengers():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # Query all passengers
#     results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

#     session.close()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_passengers = []
#     for name, age, sex in results:
#         passenger_dict = {}
#         passenger_dict["name"] = name
#         passenger_dict["age"] = age
#         passenger_dict["sex"] = sex
#         all_passengers.append(passenger_dict)

#     return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)
