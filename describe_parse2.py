import json

with open('coffee_sales/coffee_sales.json','r') as f:
    data=json.load(f)

print(type(data))

jsonstring=json.dumps(data) #this will return a json string
# print(jsonstring)
print(type(jsonstring))

newdata=json.loads(jsonstring)
print(type(newdata))

salesdata=newdata['sales']
locations=[location['name']for location in newdata['locations']]
dates=[sale['date'] for sale in salesdata]
sales=[sale['sales'] for sale in salesdata]
coffedata={'locations':locations,'dates':dates,'sales':sales}

print(coffedata)