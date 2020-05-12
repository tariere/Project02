// var boroughs = dataZT.map(listing => listing.neighborhood_group)
// var neighborhoods = dataZT.filter(listing => listing.neighborhood_group === "Manhattan").map(listing => listing.neighborhood)

// function uniqueValues(array) {
//   return Array.from(new Set(array))
// }

console.log(dataZT)

var newData = { name :"New York City", children : [] },
    levels = ["neighborhood_group","neighborhood","room_type"];

dataZT.forEach(function(d){
    var depthCursor = newData.children;
    levels.forEach(function( property, depth )
    {
        var index;
        depthCursor.forEach(function(child,i)
        {
            if ( d[property] == child.name ) 
                index = i;
        });

        if ( isNaN(index) ) 
        {
            depthCursor.push({name : d[property], children : []});
            index = depthCursor.length - 1;
        }

        depthCursor = depthCursor[index].children;

        if ( depth === levels.length - 1 )
        {
            depthCursor.push({ name : d.price});
        }
    });
});

console.log(newData);


// Define SVG area dimensions
var svgWidth = 960;
var svgHeight = 500;

// Define the chart's margins as an object
var margin = {
  top: 60,
  right: 60,
  bottom: 60,
  left: 60
};

// Define dimensions of the chart area
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Select body, append SVG area to it, and set its dimensions
var svg = d3.select("#plot")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var dataAggregated = d3.hierarchy(newData)
  .sum((d) => d.value)
  .sort(function(a, b) { return b.height - a.height || b.value - a.value; })

var layout = d3.treemap()
  .tile(d3.treemapResquarify)
  .size([width, height])
  .paddingInner(3)

var rootWithLayout = layout(dataAggregated)

function update() {
  let selparent = dataAggregated;
  console.log(selparent)
  let nodes = svg.selectAll(".node")
    .data(rootWithLayout.leaves());

  nodes
    .enter()
    .append("rect")
    .attr("class", "node")
    .merge(nodes)
  .on("click", (d) => {
        selparent = d.parent.parent;
          x.domain([d.parent.x0, d.parent.x0 + d.parent.x1-d.parent.x0]);
          y.domain([d.parent.y0, d.parent.y0 + d.parent.y1-d.parent.y0]);
          update();
    })      
    .transition().duration(1000)
    .attr("x", (d)=> (d.x0))
    .attr("y",  (d)=> (d.y0))
    .attr("width", (d)=> (d.x1)-(d.x0))
    .attr("height", (d)=> (d.y1)-(d.y0))
    .attr("title", (d) => d.name)
    .style("fill", (d) => (d.parent ? d.parent.data.name : d.data.name))

  let parent = svg.selectAll("#parent")
      .data([""])

  parent.enter()
    .append("rect")
    .attr("id","parent")    
    .merge(parent)
    .on("click", () => {
            x.domain([selparent.x0, selparent.x1-selparent.x0]);
            y.domain([selparent.y0, selparent.y1-selparent.y0]);
            update();
    })    
    .style("fill", "orange")
    .transition().duration(1000)
    .attr("x", 0)
    .attr("y", 0)
    .attr("width", width)
    .attr("height", height)    
}

update();