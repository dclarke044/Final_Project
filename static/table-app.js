var tbody = d3.select("tbody");

console.log(data);
data.forEach((meteorite) => {
  var row = tbody.append("tr");
  Object.entries(meteorite).forEach(([key, value]) => {
    var cell = row.append("td");
    cell.text(value);
  });
});

$(document).ready( function () {
  $('#movie-table').DataTable();
} );