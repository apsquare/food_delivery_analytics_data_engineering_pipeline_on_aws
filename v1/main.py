import v1.Customer as Customer ,v1.DeliveryPartner as DeliveryPartner ,v1.Order as Order ,v1.Provider as Provider ,v1.Restaurant as Restaurant
import csv 
import os 


customer = Customer.Customer()
delivery_partner = DeliveryPartner.DeliveryPartner()
restaurant = Restaurant.Restaurant()
order = Order.Order(customer.customer_id,restaurant.restaurant_id,delivery_partner.delivery_partner_id)


restaurants_file = "restaurants.csv"
orders_file = "orders.csv"
customers_file = "customers.csv"
delivery_partners_file = "delivery_partners.csv"



#Creating restaurants.csv
restaurant_exists = os.path.exists(restaurants_file)
with open(restaurants_file,'a',newline='') as rf:
  writer =  csv.writer(rf)
  if not restaurant_exists : 
    writer.writerow(["restaurant_id","restaurant_name","city","cuisine_type","rating"])
  writer.writerow([restaurant.restaurant_id,restaurant.restaurant_name,restaurant.city,restaurant.cuisine_type,restaurant.rating])

#creating orders.csv
order_exits = os.path.exists(orders_file)
with open(orders_file,'a',newline='') as of:
  writer =  csv.writer(of)
  if not order_exits : 
    writer.writerow(["order_id","customer_id","restaurant_id","delivery_partner_id","order_date","order_amount","order_status","payment_method","city"])
  writer.writerow([order.order_id,order.customer_id,order.restaurant_id,order.delivery_partner_id,order.order_date,order.order_amount,order.order_status,order.payment_method,order.city])


#creating customers.csv
customer_exists = os.path.exists(restaurants_file)
with open(customers_file,'a',newline='') as cf:
  writer =  csv.writer(cf)
  if not customer_exists : 
    writer.writerow(["customer_id","customer_name","city","customer_type","signup_date"])
  writer.writerow([customer.customer_id,customer.customer_name,customer.city,customer.customer_type,customer.signup_date])

#creating delivery_partners.csv
delivery_partner_exists = os.path.exists(delivery_partners_file)
with open(delivery_partners_file,'a',newline='') as dpf:
  writer =  csv.writer(dpf)
  if not delivery_partner_exists : 
    writer.writerow(["delivery_partner_id","delivery_partner_name","city","vehicle","joining_date"])
  writer.writerow([delivery_partner.delivery_partner_id,delivery_partner.delivery_partner_name,delivery_partner.city,delivery_partner.vehicle,delivery_partner.joining_date])




