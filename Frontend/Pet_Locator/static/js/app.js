// Create the introduction text and append it to the <p> tag
var intro = "Welcome to the Lost Pet Locator! Here you can report a lost pet or that you found a pet. You may even like to browse a geographical map to see all the reported lost pets in your neighborhood.";

d3.select(".jumbotron").selectAll("p")
    .text(intro)
    .enter()
    .html(function(d) {
        return d;
    });

// Create a header for the h2 tag
var choiceTitle = "What type of report would you like to file?";

d3.select(".choice").selectAll("h2")
    .text(choiceTitle)
    .enter()
    .html(function(d) {
        return d;
    });

// Create a header for map h2 tag
var mapTitle = "Click on the button below to view all the reported lost/found pets";

d3.select(".Map").selectAll("h2")
    .text(mapTitle)
    .enter()
    .html(function(d) {
        return d;
    });