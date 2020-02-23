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
from geojsonify import geojsonify

# Flask setup
app = Flask(__name__)

# Database setup
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/Pets.sqlite"
db = SQLAlchemy(app)

# Import the Lost and Found classes
# from .models import Lost, Found

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


if __name__ == "__main__":
    app.run()