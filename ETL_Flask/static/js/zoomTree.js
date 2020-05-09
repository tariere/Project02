console.log(data)



//     d3.csv("./assets/data/data.csv").then(function(newsData) {
//     console.log(newsData);

//     //data parsing
//     newsData.age = +newsData.age
//     newsData.income = +newsData.income
//     newsData.obesity = +newsData.obesity

//     // scale y to chart height
//     var yScale = d3.scaleLinear()
//     .domain(d3.extent(newsData, d => d.obesity))
//     .range([chartHeight, 0]);

//     // scale x to chart width
//     var xScale = d3.scaleLinear()
//     .domain(d3.extent(newsData, d => d.age))
//     .range([0, chartWidth]);

//     // create axes
//     var yAxis = d3.axisLeft(yScale);
//     var xAxis = d3.axisBottom(xScale);

//     // set x to the bottom of the chart
//     chartGroup.append("g")
//     .attr("transform", `translate(0, ${chartHeight})`)
//     .call(xAxis);

//     // set y to the y axis
//     chartGroup.append("g")
//     .call(yAxis);

//     var ageLabel = chartGroup.append("text")
//     // Position the text
//     .attr("transform", `translate(${chartWidth / 2}, ${chartHeight+margin.bottom*(1/2) + 8})`)
//     .text("Age (Median)")
//     .attr("text-anchor", "middle")
//     .attr("font-size", "16px")
//     .attr("fill", "Black");

//     var obesityLabel = chartGroup.append("text")
//     .attr("transform", `translate(${(-margin.left)*(1/2)},${chartHeight/2})rotate(-90)`)
//     .text("Obesity (%)")
//     .attr("text-anchor", "middle")
//     .attr("font-size", "16px")
//     .attr("fill", "Black");


//     // Create the rectangles using data binding
//     var circlesGroup = chartGroup.selectAll("circle")
//     .data(newsData)
//     .enter()
//     .append("circle")
//     .attr("cx", (d, i) => xScale(newsData[i].age))
//     .attr("cy", (d, i) => yScale(newsData[i].obesity))
//     .attr("r", "10")
//     .attr("stroke", "black")
//     .attr("fill", "blue")
//     .attr("opacity", 0.50);

//     var textGroup = chartGroup.selectAll(null)
//     .data(newsData)
//     .enter()
//     .append("text")
//     .attr("x", (d, i) => xScale(newsData[i].age))
//     .attr("y", (d, i) => yScale(newsData[i].obesity))
//     .text((d,i) => (newsData[i].abbr))
//     .attr("font-size", "10px")
//     .attr("text-anchor", "middle")
//     .attr("alignment-baseline", "middle")
//     .attr("fill", "white")

//     })   
// }

// makeResponsive();

// d3.select(window).on("resize", makeResponsive);