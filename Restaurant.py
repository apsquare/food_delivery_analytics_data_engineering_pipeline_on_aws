from faker import Faker
from Provider import restaurant_signup_date,  city_coordinates, timestamp
from random import randint , choice
from uuid import uuid4
import csv
import requests

fake = Faker("en_In")

#using the openpass api to get the restaurant details 
url = "https://overpass-api.de/api/interpreter"


query = f"""
[out:json][timeout:25];

node
  ["amenity"="restaurant"]
  {city_coordinates};

out;
"""

headers = {
    "User-Agent": "food-delivery-project"
}


try : 
  response = requests.post(
      url,
      data=query,
      headers=headers
  )

  if response.status_code != 200 :
    raise Exception("Bad request")
  
  data = response.json()
  restaurants = data.get("elements",[])
  if restaurants :
    restaurant = choice(restaurants)
    restaurant_name  = restaurant.get("tags",{}).get("name","Unknown Restaurant")
    restaurant_lat = restaurant.get("lat")
    restaurant_lng = restaurant.get("lon")
    cuisine_text = restaurant.get("tags", {}).get("cuisine", "")
    restaurant_cuisine = cuisine_text.split(";") if cuisine_text else []
  else :
    raise Exception("No restaurants found in the region")
  
except Exception as e: 
  print(e)
  restaurant_name = "Unknown Restaurant"
  restaurant_lat = 0.0
  restaurant_lng = 0.0
  restaurant_cuisine = []






class Restaurant : 
  def __init__(self):
    self.restaurant_id = uuid4()
    self.restaurant_name = restaurant_name
    self.address_details = (restaurant_lat,restaurant_lng)
    self.cuisine_details  = restaurant_cuisine
    self.closing_time = fake.time()
    self.rating = randint(1,5)
    self.signup_date = restaurant_signup_date
    self.owner_name = fake.name()

  def __str__(self):
      return (
           "Restaurant-Details\n"
          f"Restaurant ID      : {self.restaurant_id}\n"
          f"Restaurant Name    : {self.restaurant_name}\n"
          f"Address Details    : {self.address_details}\n"
          f"Cuisine Details    : {self.cuisine_details}\n"
          f"Closing Time       : {self.closing_time}\n"
          f"Rating             : {self.rating}\n"
          f"Signup Date        : {self.signup_date}\n"
          f"Owner Name         : {self.owner_name}"
          "\n\n\n\n"
      )
  
  def write_to_file (self):
    headers = ["restaurant_id","restaurant_name","address_details","cuisine_details","closing_time","rating","signup_date","owner_name"]
    with open(f"restaurants-{timestamp}.csv", "w", newline="") as file :
       writer = csv.writer(file)
       writer.writerow(headers)
       writer.writerow([self.restaurant_id,self.restaurant_name,self.address_details,self.cuisine_details,self.closing_time,self.rating,self.signup_date,self.owner_name])


r = Restaurant()
r.write_to_file()