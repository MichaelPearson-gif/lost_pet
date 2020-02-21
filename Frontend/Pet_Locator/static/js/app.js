// Create the introduction text and append it to the <p> tag
var intro = "Welcome to the Lost Pet Locator! Here you can report a lost pet or that you found a pet. You may even like to browse a geographical map to see all the reported lost pets in your neighborhood."

d3.select(".jumbotron").selectAll("p")
    .text(intro)
    .enter()
    .html(function(d) {
        return d;
    });
