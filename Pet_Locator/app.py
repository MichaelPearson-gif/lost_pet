# Import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from datetime import datetime

# Flask setup
app = Flask(__name__)

# Database setup
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/Pets.sqlite"
db = SQLAlchemy(app)

# Import the Lost and Found classes
from .models import Lost, Found

# Create the route to render to the index.html template
@app.route("/")
def home():
    return render_template("index.html")