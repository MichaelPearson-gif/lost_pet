# Import the database
from .app import db

# Create the lost pets table
class Lost(db.Model):
    __tablename__ = 'lost_pets'

    # Create the columns
    id = db.Column(db.Integer, primary_key=True)
    # name = name of the pet
    name = db.Column(db.Text)
    # pet_type = type of animal, i.e. dog, cat, etc.
    pet_type = db.Column(db.Text)
    age = db.Column(db.Float)
    street_add = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    zip_code = db.Column(db.Float)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    # owner = owner's name
    owner = db.Column(db.Text)
    phone = db.Column(db.Text)
    email = db.Column(db.Text)
    date = db.Column(db.Text)
    time = db.Column(db.Text)
    # description = pet's appearance and behaviors
    description = db.Column(db.Text)
    return_street_add = db.Column(db.Text)
    return_city = db.Column(db.Text)
    return_state = db.Column(db.Text)
    return_zip_code = db.Column(db.Float)

    def __repr__(self):
        return '<Lost %r>' % (self.name)

# Create the found pets table
class Found(db.Model):
    __tablename__ = 'found_pets'

    # Create the columns
    id = db.Column(db.Integer, primary_key=True)
    # pet_type = type of animal, i.e. dog, cat, etc.
    pet_type = db.Column(db.Text)
    age = db.Column(db.Float)
    street_add = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    zip_code = db.Column(db.Float)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    # founder = name of the person who found the pet
    founder = db.Column(db.Text)
    phone = db.Column(db.Text)
    email = db.Column(db.Text)
    date = db.Column(db.Text)
    time = db.Column(db.Text)
    # aquired = yes or no if the person was able to catch the lost pet
    aquired = db.Column(db.Text)
    # description = pet's appearance and behaviors
    description = db.Column(db.Text)

    def __repr__(self):
        return '<Found %r>' % (self.pet_type)

