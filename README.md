# Weather Data - RESTful API
_RESTful API for Historical Weather Information and Forecast using Python Django Rest Framework and Swagger API._

### AIM:
Creating a RESTful Web service API that provides historical data of weather and forecast weather information for given date.

### WORKING:

RESTful Web services is deployed using swagger to host Weather Information and forecast. Following endpoints are created to perform

#### 1.	Weather historical data - all dates display:

_Methods:_

##### GET 
Displays list of all the dates for which weather information is available in the database in JSON format. 

##### POST
Adds the weather information for a particular date based on the data provided

#### 2.	Weather historical data - specific date information display:

_Methods:_

##### GET
Displays weather information including maximum temperature and minimum temperature for a particular date. 
If no information is available - 404 error is displayed

##### DELETE
Deletes the weather information for a specified date

#### 3.	Weather forecast data - for week:

_Methods:_

##### GET
Displays weather forecast information for 7 days including the date mentioned in the endpoint URL.

### TECHNOLOGIES USED:

* Programming language : Python
* Framework :  		Django Rest Framework
* WebAPI : 			Swagger
* DB     : 			SQLite (Django Internal)
* Testing :			Postman API

A database is created in which a table accepts a .csv file to insert data into it.

### PARAMETERS (INPUT & OUTPUT):

* DATE: String
* TMIN:  Integer
* TMAX: Integer

##### Accepted Input URLs: 
* http://18.219.211.65:8000/historical/
* http://18.219.211.65:8000/historical/20130101
* http://18.219.211.65:8000/forecast/20130101
* http://18.219.211.65:8000/historical/<with data> (for POST)


##### Historical Data
It returns a JSON string of daily.csv, which is stored in the sqlite database in Django framework

##### Forecast Data
It returns the DATE, TMAX and TMIN for a 7 days including the date provided in JSON format.

### RESOURCES :

* http://www.django-rest-framework.org/
* https://django-rest-swagger.readthedocs.io/en/latest/

### LINKS:
* "app_url"  :   	"http://18.219.211.65:8000/", 
* "code_url": 	"https://github.uc.edu/bundeyyn/weather-restapi.git", 
* "doc_url"  : 	"https://github.uc.edu/bundeyyn/weather-restapi/blob/master/README.md"
