// Load the data from both tables
var lostData = "/api/map/lost";

var foundData = "/api/map/found";

// Print to the data to the console to ensure it comes in correctly
// d3.json(lostData, function(data) {
//     console.log(data.features);
// });

// d3.json(foundData, function(data) {
//     console.log(data.features);
// });

function getIcon(animal) {

    // Using conditional statements to choose which icon to input
    if (animal === "dog") {
        return '<i class="fa fa-dog"></i>';
    }
    else if (animal === "cat") {
        return '<i class="fa fa-cat"></i>';
    } 
    else if (animal === "frog") {
        return '<i class="fa fa-frog"></i>';
    }
    else if (animal === "bird") {
        return '<i class="fa fa-feather"></i>';
    }
    else if (animal === "spider") {
        return '<i class="fa fa-spider"></i>';
    }
    else {
        return '<i class="fa fa-paw"></i>';
    }
};

// Perform a request of the lost pet data
d3.json(lostData, function(data1) {

    d3.json(foundData, function(data2) {

        // Send the responses to the createFeatures function
        createFeatures(data1.features, data2.features);
    });
});

// Design the createFeatures function
function createFeatures(lost, found) {

    // Define a function to run on each feature for the lost pet data
    function LOnEachFeatures(feature, layer) {

        // Design the pop-ups
        layer.bindPopup("<h3>Missing: " + feature.properties.Pet_Name +
        "</h3><hr><p>Missing since: " + feature.properties.Date + " at " + feature.properties.Time +
        "</p><hr><p>Species: " + feature.properties.Pet_Type + 
        "</p><hr><p>Age: " + feature.properties.Age + 
        "</p><hr><p>Description: " + feature.properties.Description + 
        "</p><hr><p>Contact " + feature.properties.Owner + " at " + feature.properties.Phone + " or " + feature.properties.Email + 
        "</p><hr><p>Return to " + feature.properties.Return_Street_Add + " " + feature.properties.Return_City + 
        ", " + feature.properties.Return_State + " " + feature.properties.Return_Zip_Code + "</p>");
    }

    // Define a function to run on each feature for the found pet data
    function FOnEachFeatures(feature, layer) {

        // Design the pop-ups
        layer.bindPopup("<h3>Found " + feature.properties.Pet_Type +
        "</h3><hr><p>Found on: " + feature.properties.Date + "at " + feature.properties.Time +
        "</p><hr><p>Approximate age: " + feature.properties.Age + 
        "</p><hr><p>Description: " + feature.properties.Description + 
        "</p><hr><p>Is pet contained? " + feature.properties.Aquired +
        "</p><hr><p>Contact " + feature.Founder + " at " + feature.properties.Phone + " or " + feature.properties.Email + "</p>");

    }

    // Create a function that will build an icon for lost pets
    function createLMarker (feature) {
        var lostMarker = L.divIcon({
            html: getIcon(feature.properties.Pet_Type),
            iconSize: [20, 20],
            className: 'lostDivIcon'
        });

        return lostMarker;
    }

    // Create a function that will build an icon for the found pets
    function createFMarker (feature) {
        var foundMarker = L.divIcon({
            html: getIcon(feature.properties.Pet_Type),
            iconSize: [20, 20],
            className: 'foundDivIcon'
        });

        return foundMarker;
    }

    // Define a function to design the marker for the lost pet data
    function LPointToLayer (feature, latlng) {
        return L.marker(latlng, {
            icon: createLMarker(feature)
        });
    }

    // Define a function to design the marker for the found pet data
    function FPointToLayer(feature, latlng) {
        return L.marker(latlng, {
            icon: createFMarker(feature)
        });
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

    // Sending the layer to the createMap function
    createMap(lostLayer, foundLayer);
}

// Define the createMap function
function createMap(lostLayer, foundLayer) {

    // Define the tile layer
    var streetMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.streets",
        accessToken: API_KEY
    });

    // Create a baseMaps object to hold the streetmap layer
    var baseMaps = {
        "Street Map": streetMap
    };

    // Create an overlayMaps object to hold the lost and found pet layers
    var overlayMaps = {
        "Lost Pets": lostLayer,
        "Found Pets": foundLayer
    };

    // Create the map object
    var myMap = L.map("map", {
        center: [37.0902, -95.7129],
        zoom: 5,
        layers: [streetMap, lostLayer, foundLayer]
    });

    // Create a layer control to pass in the baseMaps and overlayMaps, then add it to the map
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(myMap);
}

