# Import the database
from .app import db

# Create the lost pets table
class Lost(db.Model):
    __tablename__ = 'lost_pets'

    # Create the columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    pet_type = db.Column(db.Text)
    age = db.Column(db.Float)
    street_add = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    zip_code = db.Column(db.Float)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    owner = db.Column(db.Text)
    phone = db.Column(db.Text)
    email = db.Column(db.Text)
    description = db.Column(db.Text)
