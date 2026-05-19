from uuid import uuid4
from random import choice , randint , uniform
from Provider import   max_coordinates ,customer_signup_date ,city_choosen, timestamp
from faker import Faker

import csv

fake = Faker("en_IN")

device_types = ["laptop,smart_phone,tablet,smartwatch,voice_assistant"]

cuisines = [
    "Indian",
    "Chinese",
    "Italian",
    "Mexican",
    "Thai"
]



delivery_location =  (uniform(max_coordinates[city_choosen]["max_lat"],max_coordinates[city_choosen]["min_lat"]),uniform(max_coordinates[city_choosen]["max_lng"],max_coordinates[city_choosen]["min_lng"]))



class Customer :
  def __init__(self):

    #Technical Data
    self.device_type = choice(device_types)
    self.ip_address = str(fake.ipv4())
    self.cancellation_count = randint(0,30)
    self.complaints_raised = randint(1,10)
    self.items_in_cart = randint(1,10)
    self.average_time_spent = randint(0,59)

    #Personal Data
    self.customer_id = str(uuid4())
    self.customer_name = fake.name()
    self.phone_number = fake.phone_number()
    self.delivery_location = delivery_location
    self.signup_date = customer_signup_date
    self.customer_type = choice(["regular","premium"])

    #Food Preference
    self.dietary_preference = choice(["vegetarian","non-vegetarian"])
    self.cuisine_preference = choice(cuisines)

  def __str__(self):
    return (
         "Customer-Details\n"
        f"Customer ID            : {self.customer_id}\n"
        f"Customer Name          : {self.customer_name}\n"
        f"Phone Number           : {self.phone_number}\n"
        f"Delivery Location      : {self.delivery_location}\n"
        f"Signup Date            : {self.signup_date}\n"
        f"Customer Type          : {self.customer_type}\n"
        f"Dietary Preference     : {self.dietary_preference}\n"
        f"Cuisine Preference     : {self.cuisine_preference}\n"
        f"Device Type            : {self.device_type}\n"
        f"IP Address             : {self.ip_address}\n"
        f"Cancellation Count     : {self.cancellation_count}\n"
        f"Complaints Raised      : {self.complaints_raised}\n"
        f"Items In Cart          : {self.items_in_cart}\n"
        f"Average Time Spent     : {self.average_time_spent} mins"
        "\n\n\n\n"
    )
  
  def write_to_file (self) :
    #Creating a csv file for each customer : customers.csv
    header = ["device_type","ip_address","cancellation_count","complaints_raised","items_in_cart","average_time_spent","customer_id","customer_name","phone_number","delivery_location","signup_date","customer_type","dietary_preference","cuisine_preference"]

    with open(f"customers-{timestamp}.csv","w",newline="") as file:
      writer = csv.writer(file)
      writer.writerow(header)
      writer.writerow([self.device_type,self.ip_address,self.cancellation_count,self.complaints_raised,self.items_in_cart,self.average_time_spent,self.customer_id,self.customer_name,self.phone_number,self.delivery_location,self.signup_date,self.customer_type,self.dietary_preference,self.cuisine_preference])


c = Customer()
c.write_to_file()


