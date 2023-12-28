import json

with open('coffee_sales/coffee_sales.json','r') as f:
    data=json.load(f)

print(type(data))

jsonstring=json.dumps(data) #this will return a json string
# print(jsonstring)
print(type(jsonstring))

newdata=json.loads(jsonstring)
print(type(newdata))