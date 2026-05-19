from uuid import uuid4
from time import strftime 
from random import uniform ,randint ,choice
from faker import Faker
import v1.Provider as Provider
fake= Faker('en_In')



class Order :
  def __init__(self,customer_id,restaurant_id,delivery_partner_id):
    self.order_id = str(uuid4())
    self.customer_id = customer_id
    self.restaurant_id = restaurant_id
    self.delivery_partner_id =  delivery_partner_id
    self.order_date = Provider.order_date.strftime("%d-%m-%Y")
    self.order_amount = '₹' + str(randint(100,10000))
    self.order_status = choice(['Delivered', 'Cancelled', 'In Progress'])
    self.payment_method = choice(['UPI', 'Card', 'Cash', 'Wallet'])
    self.city = Provider.city


  def display(self):
    print(self.order_id)
    print(self.customer_id)
    print(self.restaurant_id)
    print(self.delivery_partner_id)
    print(self.order_date)
    print(self.order_amount)
    print(self.order_status)
    print(self.payment_method)
    print(self.city)



    
    
  


