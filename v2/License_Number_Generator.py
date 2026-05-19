
import random
def generate_license_number():
  state_codes = ["KA", "MH", "DL", "TN", "TS"]
  state = random.choice(state_codes)
  rto = random.randint(1, 99)
  year = random.randint(2015, 2026)
  number = random.randint(10000, 99999)
  license_number = f"{state}{rto:02d} {year}{number}"
  return license_number
