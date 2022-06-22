var dataarr = eval(graphdata)
main()
function main(){
    google.load('visualization', "1", {packages:['corechart']});
    google.charts.setOnLoadCallback(drawChart);
}
function drawChart(){
    var data = google.visualization.arrayToDataTable([
        ["Tech Involved", "Number of Incidents"],
        ["Virtual Reality", dataarr[0]],
        ["Cryptocurrency", dataarr[1]],
        ["Online Games", dataarr[2]]
    ]);
    var options = {
        title: 'Tech Involved in Metaverse Crimes',
        width: 400,
        height: 300
    };
    var chart = new google.visualization.PieChart(document.getElementById('big_graph'));
    chart.draw(data, options);
}