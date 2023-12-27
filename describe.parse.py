import json
import os

jsonpath='coffee_sales'

for file in os.listdir(jsonpath):
    if file.endswith('.json'):
        with open(os.path.join(jsonpath,file)) as f:
            data=json.load(f)
            print('file :',file)
            print('type: ',type(data))

            if isinstance(data,list):
                print("list items:")
                for item in data:
                    print(item)

            elif isinstance(data,dict):
                print("dictionary items:")
                for key,value in data.items():
                    print(key,':',value)

            else:
                print('data: ')
                print(data)
            print("-------------")

