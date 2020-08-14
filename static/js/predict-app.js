var button = d3.select("#button")

button.on("click", runEnter)

function runEnter() {
    d3.event.preventDefault();
    var inputYear = d3.select("#inputYear");
    var yearValue = inputYear.property("value");
    var inputDuration = d3.select("#inputDuration");
    var durationValue = inputDuration.property("value");
    var inputBudget = d3.select("#inputBudget");
    var budgetValue = inputBudget.property("value");
    var inputGenre = d3.select("#inputGenre");
    var genreValue = inputGenre.property("value");
    var inputDirector = d3.select("#inputDirector");
    var directorValue = inputDirector.property("value");

    console.log(yearValue);
    console.log(durationValue);
    console.log(budgetValue);
    console.log(genreValue);
    console.log(directorValue);


}