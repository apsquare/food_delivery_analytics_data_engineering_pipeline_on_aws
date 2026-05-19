from geopy.distance import geodesic
from uuid import uuid4
from Customer import Customer
from DeliveryPartner import DeliveryPartner 
from Restaurant import Restaurant
from Provider import order_date , timestamp
from faker import Faker
from random import randint , choice
import csv





#Assumptions :
#The cost of each item is ₹10
#The cost of delivery is ₹0.1 per unit distance


payment_modes = [
    "Cash",
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking",
    "Wallet",
    "Paytm",
    "Google Pay",
    "PhonePe",
    "Amazon Pay",
    "EMI",
    "Gift Card",
    "Cash on Delivery",
    "Buy Now Pay Later"
]


fake = Faker("en_IN")

customer = Customer()
restaurant = Restaurant()
delivery_partner = DeliveryPartner()

pickup_location = restaurant.address_details
delivery_location = customer.delivery_location

distance = geodesic(pickup_location, delivery_location).km
print(distance)

class Orders :
  def __init__(self):
    self.order_id = uuid4()
    self.customer_id = customer.customer_id
    self.customer_name = customer.customer_name
    self.restaurant_id = restaurant.restaurant_id
    self.restaurant_name = restaurant.restaurant_name
    self.partner_id =delivery_partner.partner_id
    self.partner_name = delivery_partner.partner_name
    self.order_date = order_date
    self.order_time = fake.time()
    self.total_items = randint(1,10)
    self.distance_travelled = distance
    self.delivery_cost = distance * 0.1
    self.pickup_location = pickup_location
    self.delivery_location =delivery_location
    self.payment_method = choice(payment_modes)
    self.total_amount = str(f"₹{self.total_items*10 + self.delivery_cost}")
  
  def __str__(self):
    return (
         "Order-Details\n"
        f"Order ID           : {self.order_id}\n"
        f"Customer           : {self.customer_name} ({self.customer_id})\n"
        f"Restaurant         : {self.restaurant_name} ({self.restaurant_id})\n"
        f"Delivery Partner   : {self.partner_name} ({self.partner_id})\n"
        f"Order Date         : {self.order_date}\n"
        f"Order Time         : {self.order_time}\n"
        f"Total Items        : {self.total_items}\n"
        f"Distance Travelled : {self.distance_travelled:.2f} km\n"
        f"Delivery Cost      : ₹{self.delivery_cost:.2f}\n"
        f"Pickup Location    : {self.pickup_location}\n"
        f"Delivery Location  : {self.delivery_location}\n"
        f"Payment Method     : {self.payment_method}\n"
        f"Total Amount       : {self.total_amount}"
        "\n\n\n\n"
    )
  
  def write_to_file(self):
    headers = ["order_id","customer_id","customer_name","restaurant_id","restaurant_name","partner_id","partner_name","order_date","order_time","total_items","distance_travelled","delivery_cost","pickup_location","delivery_location","payment_method","total_amount"]

    with open(f"orders-{timestamp}.csv", "w", newline="") as file:
      writer = csv.writer(file)
      writer.writerow(headers)
      writer.writerow([self.order_id,self.customer_id,self.customer_name,self.restaurant_id,self.restaurant_name,self.partner_id,self.partner_name,self.order_date,self.order_time,self.total_items,self.distance_travelled,self.delivery_cost,self.pickup_location,self.delivery_location,self.payment_method,self.total_amount])



o = Orders()
o.write_to_file()