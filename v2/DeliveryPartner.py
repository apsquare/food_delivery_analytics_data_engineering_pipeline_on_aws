from Provider import partner_signup_date ,timestamp
from uuid import uuid4
from faker import Faker
from random import choice , randint
from License_Number_Generator import generate_license_number
import csv 
fake = Faker("en_In")
license_expiry = fake.date_between(
    start_date='today',
    end_date='+3y'
)

vehicles = [
    "Scooter",
    "Bike",
    "Electric Scooter",
    "Bicycle"
]


class DeliveryPartner :
  def __init__(self):
    self.partner_id = uuid4()
    self.partner_name = fake.name()
    self.signup_date = partner_signup_date
    self.vehicle_type = choice(vehicles)
    self.license_number = generate_license_number()
    self.license_expiry_date  = license_expiry
    self.rating = randint(1,5)
    self.emergency_contact = fake.phone_number()

  def __str__(self):
      return (
           "DeliveryPartner-Details\n"
          f"Partner ID           : {self.partner_id}\n"
          f"Partner Name         : {self.partner_name}\n"
          f"Signup Date          : {self.signup_date}\n"
          f"Vehicle Type         : {self.vehicle_type}\n"
          f"License Number       : {self.license_number}\n"
          f"License Expiry Date  : {self.license_expiry_date}\n"
          f"Rating               : {self.rating}\n"
          f"Emergency Contact    : {self.emergency_contact}"
          "\n\n\n\n"
      )
  
  def write_to_file(self):
     headers = ["partner_id","partner_name","signup_date","vehicle_type","license_number","license_expiry_date","rating","emergency_contact"]
     with open(f"delivery_partner-{timestamp}.csv","w",newline="") as file :
         writer = csv.writer(file)
         writer.writerow(headers)
         writer.writerow([self.partner_id,self.partner_name,self.signup_date,self.vehicle_type,self.license_number,self.license_expiry_date,self.rating,self.emergency_contact])

dp = DeliveryPartner()
dp.write_to_file()
