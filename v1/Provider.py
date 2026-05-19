from faker import Faker

fake = Faker('en_IN')
city = fake.city()


#Delivery partner joining date 
joining_date = fake.date_between(
  start_date='-10y',
  end_date='today'
)

#customer signup_date
signup_date = fake.date_between(
    start_date="-10y",
    end_date='today'
)


#order_date
date = max(joining_date,signup_date)
order_date = fake.date_between(
  start_date=date,
  end_date='today'
)

# print(signup_date)
# print(order_date)
# print(joining_date)