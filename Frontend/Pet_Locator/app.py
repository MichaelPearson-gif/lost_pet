# Import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from datetime import datetime

# Import geojsonify converter
from .geojsonify import geojsonify

# Flask setup
app = Flask(__name__)

# Database setup
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///./db/Pet_Tracker.sqlite"
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/Pet_Tracker.sqlite"

db = SQLAlchemy(app)

# Import the Lost and Found classes
from .models import Lost, Found

# Create the route to render to the index.html template
@app.route("/")
def home():
    return render_template("index.html")

# Query the database and send the jsonified results for the lost and pet tables
# Lost Pet
@app.route("/lost_send", methods=["GET", "POST"])
def Lsend():
    if request.method == "POST":
        id = request.form["petID"]
        name = request.form["petName"]
        pet_type = request.form["petType"]
        age = request.form["petAge"]
        street_add = request.form["lostStreetAddress"]
        city = request.form["lostCity"]
        state = request.form["lostState"]
        zip_code = request.form["lostZipCode"]
        lat = request.form["petLat"]
        lng = request.form["petLng"]
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

        lost_pet = Lost(id=id, name=name, pet_type=pet_type, age=age, street_add=street_add, city=city, state=state, zip_code=zip_code, lat=lat, lng=lng, owner=owner, phone=phone, email=email, date=date, time=time, description=description, return_street_add=return_street_add, return_city=return_city, return_state=return_state, return_zip_code=return_zip_code)
        db.session.add(lost_pet)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("lost.html")

# Found Pet
@app.route("/found_send", methods=["GET", "POST"])
def Fsend():
    if request.method == "POST":
        id = request.form["petID"]
        pet_type = request.form["petType"]
        age = request.form["petAge"]
        street_add = request.form["streetAddress"]
        city = request.form["City"]
        state = request.form["State"]
        zip_code = request.form["ZipCode"]
        lat = request.form["petLat"]
        lng = request.form["petLng"]
        founder = request.form["founderName"]
        phone = request.form["founderPhone"]
        email = request.form["founderEmail"]
        date = request.form["foundDate"]
        time = request.form["foundTime"]
        aquired = request.form["Aquired"]
        description = request.form["petDescription"]

        found_pet = Found(id=id, pet_type=pet_type, age=age, street_add=street_add, city=city, state=state, zip_code=zip_code, lat=lat, lng=lng, founder=founder, phone=phone, email=email, date=date, time=time, aquired=aquired, description=description)
        db.session.add(found_pet)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("found.html")

# This route will be used for the map to show all the reported lost pets
@app.route("/api/map/lost")
def lost_map():

    # List object to hold all the info I want to query from the DB
    sel = [
        Lost.id,
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
    lost_pet = {}
    for result in results:
        lost_pet["ID"] = result[0]
        lost_pet["Pet Name"] = result[1]
        lost_pet["Pet Type"] = result[2]
        lost_pet["Pet Age"] = result[3]
        lost_pet["Street Address"] = result[4]
        lost_pet["City"] = result[5]
        lost_pet["State"] = result[6]
        lost_pet["Zip Code"] = result[7]
        lost_pet["lat"] = result[8]
        lost_pet["lng"] = result[9]
        lost_pet["Owner's Name"] = result[10]
        lost_pet["Owner's Phone Number"] = result[11]
        lost_pet["Owner's Email"] = result[12]
        lost_pet["Date"] = result[13]
        lost_pet["Time"] = result[14]
        lost_pet["Description"] = result[15]
        lost_pet["Return Street Address"] = result[16]
        lost_pet["Return City"] = result[17]
        lost_pet["Return State"] = result[18]
        lost_pet["Return Zip Code"] = result[19]

    # Returning the dictionary as a geojson objet
    return geojsonify(lost_pet)

# This route will be used for the map to show all the reported found pets
@app.route("/api/map/found")
def found_map():

    # List object to hold all the info I want to query from the DB
    sel = [
        Found.id,
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
    found_pet = {}
    for result in results:
        found_pet["ID"] = result[0]
        found_pet["Pet Type"] = result[1]
        found_pet["Age"] = result[2]
        found_pet["Street Address"] = result[3]
        found_pet["City"] = result[4]
        found_pet["State"] = result[5]
        found_pet["Zip Code"] = result[6]
        found_pet["lat"] = result[7]
        found_pet["lng"] = result[8]
        found_pet["Founder's Name"] = result[9]
        found_pet["Founder's Phone"] = result[10]
        found_pet["Founder's Email"] = result[11]
        found_pet["Date"] = result[12]
        found_pet["Time"] = result[13]
        found_pet["Aquired"] = result[14]
        found_pet["Description"] = result[15]

    # Returning the dictionary as a geojson object
    return geojsonify(found_pet)



if __name__ == "__main__":
    app.run(debug=True)