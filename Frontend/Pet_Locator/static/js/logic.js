// Load the data from both tables
var lostData = "/api/map/lost";
var foundData = "/api/map/found";

// Create a function to choose the marker icon
function getIcon(animal) {

    // Using conditional statements to choose which icon to input
    if (animal === "dog") {
        return "dog";
    }
    else if (animal === "cat") {
        return "cat";
    } 
    else if (animal === "frog") {
        return "frog";
    }
    else if (animal === "bird") {
        return "feather";
    }
    else if (animal === "spider") {
        return "spider";
    }
    else {
        return "paw";
    }
}