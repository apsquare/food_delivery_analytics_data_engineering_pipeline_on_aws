from uuid import uuid4
from faker import Faker
from random import choice , randint
import v1.Provider as Provider
from v1.Customer import Customer
import csv

fake = Faker('en_IN')
print(fake.city_name())

cuisines = [
  "Indian",
  "Chinese",
  "Mexican",
  "Thai",
  "Japanese"
]


class Restaurant :

  def __init__(self):
    self.restaurant_id = str(uuid4())
    self.city = Provider.city
    self.cuisine_type = choice(cuisines)
    self.restaurant_name = fake.first_name() + f"\'s {self.cuisine_type}" + ' Restaurant'
    self.rating = randint(1,5)


  def display(self):
    print(self.restaurant_id)
    print(self.restaurant_name)
    print(self.city)
    print(self.cuisine_type)
    print(self.rating)







