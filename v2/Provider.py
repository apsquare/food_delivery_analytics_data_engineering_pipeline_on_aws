# The app is supposed to be working in only the given cities 


#We need to install faker first 
#The app is supposed to have started 3 years back


from faker import Faker
from random import choice
from datetime import datetime


timestamp = datetime.now()

max_coordinates = {

    "delhi": {
        "max_lat": 28.90,
        "min_lat": 28.40,
        "max_lng": 77.40,
        "min_lng": 76.80
    },

    "mumbai": {
        "max_lat": 19.30,
        "min_lat": 18.89,
        "max_lng": 72.99,
        "min_lng": 72.77
    },

    "bangalore": {
        "max_lat": 13.20,
        "min_lat": 12.83,
        "max_lng": 77.80,
        "min_lng": 77.46
    },

    "chennai": {
        "max_lat": 13.25,
        "min_lat": 12.85,
        "max_lng": 80.35,
        "min_lng": 80.10
    },

    "hyderabad": {
        "max_lat": 17.60,
        "min_lat": 17.20,
        "max_lng": 78.70,
        "min_lng": 78.20
    },

    "kolkata": {
        "max_lat": 22.70,
        "min_lat": 22.45,
        "max_lng": 88.50,
        "min_lng": 88.20
    },

    "pune": {
        "max_lat": 18.65,
        "min_lat": 18.40,
        "max_lng": 73.98,
        "min_lng": 73.70
    },

    "ahmedabad": {
        "max_lat": 23.15,
        "min_lat": 22.90,
        "max_lng": 72.75,
        "min_lng": 72.45
    },

    "jaipur": {
        "max_lat": 26.98,
        "min_lat": 26.75,
        "max_lng": 75.95,
        "min_lng": 75.65
    },

    "lucknow": {
        "max_lat": 26.95,
        "min_lat": 26.75,
        "max_lng": 81.10,
        "min_lng": 80.80
    },

    "kochi": {
        "max_lat": 10.10,
        "min_lat": 9.85,
        "max_lng": 76.45,
        "min_lng": 76.15
    },

    "surat": {
        "max_lat": 21.30,
        "min_lat": 21.05,
        "max_lng": 72.95,
        "min_lng": 72.70
    },

    "indore": {
        "max_lat": 22.85,
        "min_lat": 22.60,
        "max_lng": 75.95,
        "min_lng": 75.70
    },

    "bhopal": {
        "max_lat": 23.35,
        "min_lat": 23.15,
        "max_lng": 77.55,
        "min_lng": 77.25
    },

    "goa": {
        "max_lat": 15.65,
        "min_lat": 15.20,
        "max_lng": 74.10,
        "min_lng": 73.70
    }
}


fake = Faker()

customer_signup_date = fake.date_between(start_date='-3y',end_date='today')
partner_signup_date = fake.date_between(start_date='-3y',end_date='today')
restaurant_signup_date = fake.date_between(start_date='-3y',end_date='today')

#The order should be places on a date later to the customer and partner signp dates 
recent_signup = max(customer_signup_date,partner_signup_date)
order_date = fake.date_between(start_date=recent_signup,end_date='today')

# The app is supposed to be working in only the given cities 
#Selecting a city 
cities = [
    "delhi",
    "mumbai",
    "bangalore",
    "chennai",
    "hyderabad",
    "kolkata",
    "pune",
    "ahmedabad",
    "jaipur",
    "lucknow",
    "kochi",
    "surat",
    "indore",
    "bhopal",
    "goa"
]

city_choosen = choice(cities)
city_coordinates = (max_coordinates[city_choosen]["min_lat"],max_coordinates[city_choosen]["min_lng"],max_coordinates[city_choosen]["max_lat"],max_coordinates[city_choosen]["max_lng"])