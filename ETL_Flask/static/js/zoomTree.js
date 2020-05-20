var baseURL = "https://www.airbnb.com/rooms/"

// function for determining change in input field
function filterByInput(event) {
  var newText = d3.select("#input-price").node().value;
  console.log(newText)
  filteredData = dataZT.filter(d => d.price <= newText)
  d3.select("#input-price").node().value = ""
  d3.selectAll("#chart > *").remove();
  circlePack(hierarchy(filteredData));
};

// filtered data click function
d3.select("#filter-btn").on("click", filterByInput);

//Function for ordering data in hierarchy
function hierarchy(data) {
  var newData = { name :"New York City", children : [] },
    levels = ["neighborhood_group","neighborhood","room_type"];

  data.forEach(function(d){
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
            depthCursor.push({name : `$${d.price}`, size : d.price, url : `${baseURL + d.entry_id}`, description : d.name});
        }
    });
  })
  return newData
}

//function for circle packing
function circlePack(newData) {

  //define variables
  var height = 850
  var width = height

  //Append svg to chart id in html
  var svg = d3.select("#chart")
      .append("svg")
    .attr("width", width)
    .attr("height", height)
  var margin = 5
  var diameter = +svg.attr("width")

  // Append group element to svg
  var g = svg
    .append("g").attr("transform", "translate(" + diameter / 2 + "," + diameter / 2 + ")");

  var color = d3.scaleLinear()
      .domain([-1, 5])
      .range(["hsl(152,80%,80%)", "hsl(228,30%,40%)"])
      .interpolate(d3.interpolateHcl);

  var pack = d3.pack()
      .size([diameter - margin, diameter - margin])
      .padding(2);

  // create a tooltip
  var toolTip = d3.select(".row").append("div")
    .attr("class", "detail-tip");

  var root = d3.hierarchy(newData)
      .sum(function(d) { return d.size; })
      .sort(function(a, b) { return b.value - a.value; });

  var focus = root,
      nodes = pack(root).descendants(),
      view;

  // Append circles for data points
  var circle = g.selectAll("circle")
    .data(nodes)
    .enter().append("circle")
      .attr("class", function(d) { return d.parent ? d.children ? "node" : "node node--leaf" : "node node--root"; })
      .style("fill", function(d) { return d.children ? color(d.depth) : null; })
      .on("click", function(d) { if (focus !== d) zoom(d), d3.event.stopPropagation(); })
      .on("mouseover", function(d) {
        toolTip.style("display", "block");
        return d.children ? 
        toolTip.html(`Category: <strong>${d.data.name}</strong>`) //if parent element
          .style("left", d3.event.pageX + "px")
          .style("top", d3.event.pageY + "px") :
        toolTip.html(`Listing Description:<br> <strong>${d.data.description}</strong><br> *CLICK ME!*`) // if child element
          .style("left", d3.event.pageX + "px")
          .style("top", d3.event.pageY + "px")
      })
      .on("mouseout", function() {
        toolTip.style("display", "none");
      });
  // text variable for circle text
  var text = g.selectAll("text")
    .data(nodes)
    .enter().append("text")
      .attr("class", function(d) { return d.parent ? d.children ? "label" : "label label--leaf" : "label label--root"; })
      .style("fill-opacity", function(d) { return d.parent === root ? 1 : 0; })
      .style("display", function(d) { return d.parent === root ? "inline" : "none"; })
      .html(function(d) { return d.data.name; });

  var node = g.selectAll("circle,text");

  // On click functions for zoom and hyperlink
  svg
    .style("background", color(-1))
    .on("click", function() {event.target.__data__.depth === 4 ? window.open(event.target.__data__.data.url) : zoom(root); });

  zoomTo([root.x, root.y, root.r * 2 + margin]);

  // zoom function defined
  function zoom(d) {
    var focus0 = focus; focus = d;

    var transition = d3.transition()
      .duration(d3.event.altKey ? 7500 : 750)
      .tween("zoom", function(d) {
        var i = d3.interpolateZoom(view, [focus.x, focus.y, focus.r * 2 + margin]);
        return function(t) { zoomTo(i(t)); };
      });

    transition.selectAll("text")
      .filter(function(d) { return d.parent === focus || this.style.display === "inline"; })
      .style("fill-opacity", function(d) { return d.parent === focus ? 1 : 0; })
      .on("start", function(d) { if (d.parent === focus) this.style.display = "inline"; })
      .on("end", function(d) { if (d.parent !== focus) this.style.display = "none"; });
  }

  function zoomTo(v) {
    var k = diameter / v[2]; view = v;
    node.attr("transform", function(d) { return "translate(" + (d.x - v[0]) * k + "," + (d.y - v[1]) * k + ")"; });
    circle.attr("r", function(d) { return d.r * k; });
  };

}

circlePack(hierarchy(dataZT));