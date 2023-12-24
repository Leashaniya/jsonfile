# print line by line

with open('coffee_sales/coffee_sales_1.json','r') as f:
    
    for item in f:
        print(item)


#or
        
import json

with open('coffee_sales/coffee_sales_1.json','r') as f:
    data=json.load(f)
    

for item in data:
        print(item)


#or

with open('coffee_sales/coffee_sales_1.json','r') as f:
    result=f.readlines()
    

for item in result:
    print(item)
