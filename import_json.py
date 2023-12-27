import json

url='coffee_sales/coffee_sales.json'
with open(url,'r') as f:
    data=json.load(f)

    #this print only the keys that are location and sales
    # for item in data:
    #     print(item)
sales_data=data['sales']
#Using a list comprehension allows you to iterate through each dictionary in the 'locations' list and extract the 'name' key, resulting in a list of location names.
locations=[location['name'] for location in data['locations']]
dates=[sale['date'] for sale in sales_data]
sales=[sale['sales'] for sale in sales_data]

coffee_data={'locations:': locations,
             'dates: ': dates,
             'sales: ':sales}

print(coffee_data)