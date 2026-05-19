from uuid import uuid4
from faker import Faker
from random import choice
import v1.Provider as Provider

fake  = Faker('en_In')


class DeliveryPartner:
  def __init__(self):
    self.delivery_partner_id = uuid4()
    self.delivery_partner_name = fake.name()
    self.city = Provider.city
    self.vehicle = choice(['Bike','Scooter','Cycle'])
    self.joining_date = Provider.joining_date.strftime("%d-%m-%Y")

  def display(self):
    print(self.delivery_partner_id)
    print(self.delivery_partner_name)
    print(self.city)
    print(self.vehicle)
    print(self.joining_date)

# dp = DeliveryPartner()
# dp.display
