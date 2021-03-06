// Create the introduction text and append it to the <p> tag
var intro = "Welcome to the Lost Pet Locator! Here you can report a lost pet or that you found a pet. You may even like to browse a geographical map to see all the reported lost pets in your neighborhood.";

d3.select(".header").selectAll("p")
    .text(intro)
    .enter()
    .html(function(d) {
        return d;
    });

// Create a header for the h2 tag
var choiceTitle = "What type of report would you like to file?";

d3.select("#report").selectAll("h2")
    .text(choiceTitle)
    .enter()
    .html(function(d) {
        return d;
    });

// Create a header for map h2 tag
var mapTitle = "Click on the button below to view all the reported lost/found pets";

d3.select("#Map").selectAll("h2")
    .text(mapTitle)
    .enter()
    .html(function(d) {
        return d;
    });

// Creating the headers for the Lost and Found pet forms h2 tag
var lostTitle = "Please enter the information about your lost pet. Fields marked with a red asterisk must be filled in order to submit your lost pet form.";
var foundTitle = "Please enter the information about the pet you found. Fields marked with a red asterisk must be filled in order to submit your found pet form.";

d3.select(".lost-title").selectAll("h2")
    .text(lostTitle)
    .enter()
    .html(function(d) {
        return d;
    });

d3.select(".found-title").selectAll("h2")
    .text(foundTitle)
    .enter()
    .html(function(d) {
        return d;
    });
