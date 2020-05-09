import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


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
airbnb = Base.classes.airbnb_ny

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
 Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of airbnb data including all columns"""
    # Query all airbnb
    results = session.query(airbnb.entry_id, airbnb.name, airbnb.host_id, airbnb.neighbourhood_group, airbnb.neighbourhood, airbnb.latitude, airbnb.longitude, airbnb.room_type, airbnb.price, airbnb.minimum_nights, airbnb.number_of_reviews, airbnb.last_review, airbnb.reviews_per_month, airbnb.calculated_host_listings_count, airbnb.availability_365).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_airbnbs
    all_airbnb = []
    for entry_id, name, host_id, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365 in results:
        airbnb_dict = {}
        airbnb_dict["entry_id"] = entry_id
        airbnb_dict["name"] = name
        airbnb_dict["host_id"] = host_id
        airbnb_dict["neighbourhood_group"] = neighbourhood_group
        airbnb_dict["neighbourhood"] = neighbourhood
        airbnb_dict["latitude"] = latitude
        airbnb_dict["longitude"] = longitude
        airbnb_dict["room_type"] = room_type
        airbnb_dict["price"] = price
        airbnb_dict["minimum_nights"] = minimum_nights
        airbnb_dict["number_of_reviews"] = number_of_reviews
        airbnb_dict["last_review"] = last_review
        airbnb_dict["reviews_per_month"] = reviews_per_month
        airbnb_dict["calculated_host_listings_count"] = calculated_host_listings_count
        airbnb_dict["availability_365"] = availability_365
        all_airbnb.append(airbnb_dict)

    data = jsonify(all_airbnb)

    return render_template("index.html", data=data)




    

    



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
