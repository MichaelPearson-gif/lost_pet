# Import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

import datetime as dt 

# Import requests to make an API call to retrieve coordinate data
import requests

# Import json to help convert the API request into a json format
import json

# Import API key
from .config import gkey

# Import geojsonify converter
from .geojsonify import geojsonify

# Flask setup
app = Flask(__name__)

# Database setup
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/Pet_Tracker.sqlite"

db = SQLAlchemy(app)

# Import the Lost and Found classes
from .models import Lost, Found

# Create the database
@app.before_first_request
def setup():
    # db.drop_all()
    db.create_all()

# Create the route to render to the index.html template
@app.route("/")
def home():
    return render_template("index.html")

# Create the route to render to the map.html template
@app.route("/map")
def map():
    return render_template("map2.html")

# Query the database and send the jsonified results for the lost and pet tables
# Lost Pet
@app.route("/lost_send", methods=["GET", "POST"])
def Lsend():
    if request.method == "POST":
        name = request.form["petName"]
        pet_type = request.form["petType"]
        age = request.form["petAge"]
        street_add = request.form["lostStreetAddress"]
        city = request.form["lostCity"]
        state = request.form["lostState"]
        zip_code = request.form["lostZipCode"]
        # lat = request.form["petLat"]
        # lng = request.form["petLng"]
        owner = request.form["ownerName"]
        phone = request.form["ownerPhone"]
        email = request.form["ownerEmail"]
        date = request.form["lostDate"]
        time = request.form["lostTime"]
        description = request.form["petDescription"]
        return_street_add = request.form["returnStreetAddress"]
        return_city = request.form["returnCity"]
        return_state = request.form["returnState"]
        return_zip_code = request.form["returnZipCode"]

        # Making an API call to retrieve the geographical coordinates
        # Address that the API will be looking for
        target_address = f"{street_add} {city}, {state}"

        # Building the endpoint URL
        lost_url = ('https://maps.googleapis.com/maps/api/geocode/json?'
            'address={0}&key={1}').format(target_address, gkey)

        # Make the request to the endpoint and convert the result to json
        geo_data = requests.get(lost_url).json()

        # Extract the latitude and longitude
        lat = geo_data["results"][0]["geometry"]["location"]["lat"]
        lng = geo_data["results"][0]["geometry"]["location"]["lng"]

        # Convert any uppercase letters in pet_type to lowercase
        p_type = pet_type.lower()

        # Add the new data into the database
        lost_pet = Lost(name=name, pet_type=p_type, age=age, street_add=street_add, city=city, state=state, zip_code=zip_code, lat=lat, lng=lng, owner=owner, phone=phone, email=email, date=date, time=time, description=description, return_street_add=return_street_add, return_city=return_city, return_state=return_state, return_zip_code=return_zip_code)
        db.session.add(lost_pet)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("lost.html")

# Found Pet
@app.route("/found_send", methods=["GET", "POST"])
def Fsend():
    if request.method == "POST":
        pet_type = request.form["petType"]
        age = request.form["petAge"]
        street_add = request.form["streetAddress"]
        city = request.form["City"]
        state = request.form["State"]
        zip_code = request.form["ZipCode"]
        # lat = request.form["petLat"]
        # lng = request.form["petLng"]
        founder = request.form["founderName"]
        phone = request.form["founderPhone"]
        email = request.form["founderEmail"]
        date = request.form["foundDate"]
        time = request.form["foundTime"]
        aquired = request.form["Aquired"]
        description = request.form["petDescription"]

        # Making an API call to retrieve the geographical coordinates
        # Address that the API will be looking for
        target_address = f"{street_add} {city}, {state}"

        # Building the endpoint URL
        found_url = ('https://maps.googleapis.com/maps/api/geocode/json?'
            'address={0}&key={1}').format(target_address, gkey)

        # Make the request to the endpoint and convert the result to json
        geo_data = requests.get(found_url).json()

        # Extract the latitude and longitude
        lat = geo_data["results"][0]["geometry"]["location"]["lat"]
        lng = geo_data["results"][0]["geometry"]["location"]["lng"]

        # Convert any uppercase letters in pet_type to lowercase
        p_type = pet_type.lower()

        # Add the new data into the database
        found_pet = Found(pet_type=p_type, age=age, street_add=street_add, city=city, state=state, zip_code=zip_code, lat=lat, lng=lng, founder=founder, phone=phone, email=email, date=date, time=time, aquired=aquired, description=description)
        db.session.add(found_pet)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("found.html")

# This route will be used for the map to show all the reported lost pets
@app.route("/api/map/lost")
def lost_map():

    # List object to hold all the info I want to query from the DB
    sel = [
        Lost.name,
        Lost.pet_type,
        Lost.age,
        Lost.street_add,
        Lost.city,
        Lost.state,
        Lost.zip_code,
        Lost.lat,
        Lost.lng,
        Lost.owner,
        Lost.phone,
        Lost.email,
        Lost.date,
        Lost.time,
        Lost.description,
        Lost.return_street_add,
        Lost.return_city,
        Lost.return_state,
        Lost.return_zip_code
    ]

    # Query the database
    results = db.session.query(*sel).all()

    # Creating a dictionary to store the info from the db
    lost_dict = []
    for name, pet_type, age, street_add, city, state, zip_code, lat, lng, owner, phone, email, date, time, description, return_street_add, return_city, return_state, return_zip_code in results:
        lost_pet = {
            "Pet_Name" : name,
            "Pet_Type" : pet_type,
            "Age" : age,
            "Street Address" : street_add,
            "City" : city,
            "State" : state,
            "Zip Code" : zip_code,
            "lat" : lat,
            "lng" : lng,
            "Owner" : owner,
            "Phone" : phone,
            "Email" : email,
            "Date" : date,
            "Time" : time,
            "Description" : description,
            "Return_Street_Add" : return_street_add,
            "Return_City" : return_city,
            "Return_State" : return_state,
            "Return_Zip_Code" : return_zip_code
        }
        lost_dict.append(lost_pet)

    # Jsonify the data
    return geojsonify(lost_dict)

# This route will be used for the map to show all the reported found pets
@app.route("/api/map/found")
def found_map():

    # List object to hold all the info I want to query from the DB
    sel = [
        Found.pet_type,
        Found.age,
        Found.street_add,
        Found.city,
        Found.state,
        Found.zip_code,
        Found.lat,
        Found.lng,
        Found.founder,
        Found.phone,
        Found.email,
        Found.date,
        Found.time,
        Found.aquired,
        Found.description
    ]

    # Query the database
    results = db.session.query(*sel).all()

    # Creating a dictionary to store the info from the db
    found_dict = []
    for pet_type, age, street_add, city, state, zip_code, lat, lng, founder, phone, email, date, time, aquired, description in results:
        found_pet = {
            "Pet_Type" : pet_type,
            "Age" : age,
            "Street Address" : street_add,
            "City" : city,
            "State" : state,
            "Zip Code" : zip_code,
            "lat" : lat,
            "lng" : lng,
            "Founder" : founder,
            "Phone" : phone,
            "Email" : email,
            "Date" : date,
            "Time" : time,
            "Aquired": aquired,
            "Description" : description
        }
        found_dict.append(found_pet)

    # Jsonify the data
    return geojsonify(found_dict)

if __name__ == "__main__":
    app.run(debug=True)