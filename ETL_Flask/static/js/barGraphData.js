var chart = tui.chart; /* namespace */

// Testing that we have access to our data 
console.log(air_data)
console.log("hi")
console.log(air_data[0])
console.log("ola")



// Adding my data to variables 

var brooklyn = [];
var manhattan = [];
var queens = [];
var bronx = [];
var staten = [];

// Looping through my air_bnb data to append to my new list

air_data.forEach((instance) => {
    Object.entries(instance).forEach(([key,value]) => {

        // Use the value to determine which array to push the value to 
        if (value === "Brooklyn") {
            brooklyn.push(instance);
        }
        else if (value == "Manhattan") {
            manhattan.push(instance)
        }
        else if (value == "Queens") {
            queens.push(instance)
        }
        else if (value == "Bronx") {
            bronx.push(instance)
        }
        else if (value == "Staten Island") {
            staten.push(instance)
        }
    });
});

console.log(staten)

// Creating a function that counts the number of private rooms 

function privateRCount(neighborhood) {
    var count = 0;
    for (var i = 0; i < neighborhood.length; i++){
        if(neighborhood[i].room_type == "Private room")
        count++;
    }
    return count;
};

// Creating a function that counts the number of entire apartments/houses

function entireRCount(neighborhood) {
    var count2 = 0;
    for (var i = 0; i < neighborhood.length; i++){
        if(neighborhood[i].room_type == "Entire home/apt")
        count2++;
    }
    return count2;
};


// Creating a function that counts the number of shared rooms

function sharedRCount(neighborhood) {
    var count3 = 0;
    for (var i = 0; i < neighborhood.length; i++){
        if(neighborhood[i].room_type == "Shared room")
        count3++;
    }
    return count3;
};


// Creating Chart 

var container = document.getElementById('chart-area');

var data = {
    categories: ['Brooklyn', 'Manhattan', 'Queens', 'Bronx', 'Staten Island'],
    series: [
        {
            name: 'Entire Home/Apartment',
            data: [entireRCount(brooklyn), entireRCount(manhattan), entireRCount(queens), entireRCount(bronx), entireRCount(staten)]
        },
        {
            name: 'Private Room',
            data: [privateRCount(brooklyn), privateRCount(manhattan), privateRCount(queens), privateRCount(bronx), privateRCount(staten)]
        },
        {
            name: 'Shared Room',
            data: [sharedRCount(brooklyn), sharedRCount(manhattan), sharedRCount(queens), sharedRCount(bronx), sharedRCount(staten)]
        },
    ]
};
var options = {
    chart: {
        width: 1160,
        height: 650,
        title: 'Listings',
        'format': '1,000'
    },
    yAxis: {
        title: 'neighborhood'
    },
    xAxis: {
        title: 'count',
        max: 12000
    },
    series: {
        stack: 'normal'
    }
};
var theme = {
    series: {
        colors: [
            '#83b14e', '#458a3f', '#295ba0', '#2a4175', '#289399',
            '#289399', '#617178', '#8a9a9a', '#516f7d', '#dddddd'
        ]
    }
};


tui.chart.barChart(container, data, options);

