from uuid import uuid4
from faker import Faker
from random import choice
import v1.Provider as Provider
fake = Faker('en_In')


class Customer : 
  def __init__(self):
    self.customer_id = uuid4()
    self.customer_name = fake.first_name()
    self.city = Provider.city
    self.signup_date = Provider.signup_date.strftime("%d-%m-%Y")
    self.customer_type = choice(['Regular','Premium'])

  def display(self):
    print(self.city)
    print(self.customer_name)
    print(self.customer_type)
    print(self.signup_date)
    print(self.customer_id)


c = Customer()
c.display()






