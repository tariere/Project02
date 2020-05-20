# New York, New York - Selecting an AirBnB location in New York City
![NYC](ETL_Flask/Resources/Images/Jg14FgM.jpg)


### Developers
***
Leo Ramirez, Vehonti Apofka, Justin Frank, Araz Ohanessian and Tari Okoya-Koren
***
### Description
***
We took an AirBnB dataset and we have provided some additional ways to visualize the data to assist a user who is considering visiting NYC and wants to use AirBnB.

### Our approach
***
We found a data set from Kaggle.  It was pretty clean but we did take some additional steps to get the data the way we wanted.  We removed some values for listings that were not available for users, but in the dataset. We also removed listings that had not been reviewed by any previous AirBnB users. We dropped a few columns and renamed columns, ended up with about 26k rows of data to work with.  

We created a database using AWS and loaded data to it using Postgres.  Once the data was available, we pulled it using a Flask app we created and had different web pages pulling from the data sources.

### Data Set Used
***
Kaggle NYC AirBnB Open Data
* http://example.com/https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data#AB_NYC_2019.csv

Copyright Cantankerous Canines &reg;2020
