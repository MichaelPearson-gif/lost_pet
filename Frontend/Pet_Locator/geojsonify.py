# Import json in order to convert python dictionaries to json strings
import json

# Geojson is a format for encoding geographical data into json (JavaScript Object Notation)

# Create the geojsonify function that will convert python dictionaries to geojson objects
def geojsonify(data):

    # Initialize the features array
    features = []

    # Loop through the list of dictionaries
    for i in range(0, len(data)):

        # Create the coordinates array using list comprehension, which will grab the longitude and latitude
        # The function sorted() uses a keyword 'reverse' that when set to true will reverse the order.
        # This way the coordinates in the geojson object are in the form longitude, latitude
        coordinates = [value for key, value in sorted(data[i].items(), reverse=True) if key == 'lng' or key == 'lat']

        # Loop through the key and values to populate a new dictionary called properties
        # Exclude the lat and lng
        properties = {key: value for key, value in data[i].items() if key != "lat" and key != "lng"}

        # Create the key and values that will populate the features array of dictionaries
        my_features = {
            'type': 'Feature',
            'properties': properties,
            'geometry': {
                'type': 'Point',
                'coordinates': coordinates
            }
        }

        # Append to the features array
        features.append(my_features)

    # Create a new dictionary that will be the format for the geojson object
    geojson = {
        'type': 'FeatureCollection',
        'features': features
    }

    # Return the geojson object
    return json.dumps(geojson)