// Load the data from both tables
var lostData = "/api/map/lost";
var foundData = "/api/map/found";

// Create a function to choose the marker icon
function getIcon(animal) {

    // Using conditional statements to choose which icon to input
    if (animal === "dog") {
        return "fa-dog";
    }
    else if (animal === "cat") {
        return "fa-cat";
    } 
    else if (animal === "frog") {
        return "fa-frog";
    }
    else if (animal === "bird") {
        return "fa-feather";
    }
    else if (animal === "spider") {
        return "fa-spider";
    }
    else {
        return "fa-paw";
    }
};

// Perform a request of the lost pet data
d3.json(lostData, function(data1) {

    // Send the response to the createFeatures function
    createFeatures(data1.features);
});

// Perform a request of the found pet data
d3.json(foundData, function(data2) {

    // Send the response to the createFeatures function
    createFeatures(data2.features);
});

// Design the createFeatures function
// Function should spit out 2 layers that will be sent to the createMap function
function createFeatures(lost, found) {

    // Define a function to run on each feature for the lost pet data
    function LOnEachFeatures(feature, layer) {

        // Design the pop-ups
        layer.bindPopup("<h3>Missing: " + feature.properties.name +
        "</h3><hr><p>Missing since: " + feature.properties.date + "at " + feature.properties.time +
        "</p><hr><p>Species: " + feature.pet_type + 
        "</p><hr><p>Age: " + feature.properties.age + 
        "</p><hr><p>Description: " + feature.properties.description + 
        "</p><hr><p>Contact " + feature.owner + " at " + feature.properties.phone + " or " + feature.properties.email + 
        "</p><hr><p>Return to " + feature.properties.return_street_add + feature.properties.return_city + 
        ", " + feature.properties.return_state + feature.properties.return_zip_code + "</p>");
    }

    // Define a function to run on each feature for the found pet data
    function FOnEachFeatures(feature, layer) {

        // Design the pop-ups
        layer.bindPopup("<h3>Found " + feature.properties.pet_type +
        "</h3><hr><p>Found on: " + feature.properties.date + "at " + feature.properties.time +
        "</p><hr><p>Approximate age: " + feature.properties.age + 
        "</p><hr><p>Description: " + feature.properties.description + 
        "</p><hr><p>Is pet contained? " + feature.properties.aquired +
        "</p><hr><p>Contact " + feature.founder + " at " + feature.properties.phone + " or " + feature.properties.email + "</p>");

    }

    // Define an icon for lost pets
    var lostMarker = L.ExtraMarkers.icon({
        icon: getIcon(lost),
        markerColor: 'red',
        shape: 'circle',
        prefix: 'fa'
    });

    // Define an icon for the found pets
    var foundMarker = L.ExtraMarkers.icon({
        icon: getIcon(found),
        markerColor: 'blue',
        shape: 'circle',
        prefix: 'fa'
    });

    // Define a function to design the marker for the lost pet data
    function LPointToLayer (latlng) {
        return L.marker(latlng, {icon: lostMarker});
    }

    // Define a function to design the marker for the found pet data
    function FPointToLayer (latlng) {
        return L.marker(latlng, {icon: foundMarker});
    }

    // Create the GeoJson layers for the lost and found pet data

    // Lost
    var lostLayer = L.geoJSON(lost, {
        pointToLayer: LPointToLayer,
        onEachFeature: LOnEachFeatures
    });

    // Found
    var foundLayer = L.geoJSON(found, {
        pointToLayer: FPointToLayer,
        onEachFeature: FOnEachFeatures
    });

    // Sending the two layers to the createMap function
    createMap(lostLayer, foundLayer);
}