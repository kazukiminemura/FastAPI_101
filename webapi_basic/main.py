import requests
import json

url = "https://zipcloud.ibsnet.co.jp/api/search"

zip = input("Enter a postal code (e.g., 1000001): ")

param = {"zipcode": zip}

res = requests.get(url, params=param)

data = json.loads(res.text)

print(data)

print('*' * 50)

if data['results'] is None:
  address_info = data['results'][0]

  zipcode = address_info['zipcode']

  address = f"{address_info['address1']}{address_info['address2']}{address_info['address3']}"

  print(f"Postal Code: {zipcode} Address: {address}")

else:
  print("No address found for the given postal code.")