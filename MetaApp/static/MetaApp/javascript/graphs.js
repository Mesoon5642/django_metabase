var techarr = eval(graphdata)
var targetarr = eval(targetdata)
main()
function main(){
    google.load('visualization', "1", {packages:['corechart']});
    google.charts.setOnLoadCallback(drawChart);
}
function drawChart(){
    var data = google.visualization.arrayToDataTable([
        ["Tech Involved", "Number of Incidents"],
        ["Virtual Reality", techarr[0]],
        ["Cryptocurrency", techarr[1]],
        ["Online Games", techarr[2]]
    ]);
    var options = {
        title: 'Tech Involved in Metaverse Crimes',
        width: 500,
        height: 300,
        backgroundColor: "#DCDCDC"
    };
    var data1 = google.visualization.arrayToDataTable([
        ["Targets", "Number of Incidents"],
        ["Individual", targetarr[0]],
        ["School", targetarr[1]],
        ["Public Building", targetarr[2]],
        ["Crypto Exchange", targetarr[3]],
        ["Online Gaming Platform", targetarr[4]],
        ["Corporation", targetarr[5]],
        ["Online Forum", targetarr[6]],
        ["Other", targetarr[7]]
    ]);
    var options1 = {
        title: "Common Metaverse Crime Targets",
        width: 500,
        height: 300,
        backgroundColor: "#DCDCDC"
    }
    var chart = new google.visualization.PieChart(document.getElementById('big_graph'));
    var chart1 = new google.visualization.PieChart(document.getElementById("big_graph_1"));
    chart.draw(data, options);
    chart1.draw(data1, options1);
}