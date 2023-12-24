import requests
import json

url='https://jsonplaceholder.typicode.com/users'

headers={
    'Content-Type':'application/json'
}

params={
    'name':'Clementine Bauch'
}

response=requests.get(url,headers=headers,params=params)
if response.status_code==200:
    data= json.loads(response.text)
    for item in data:
        print(item)
else:
    print("error fetching data with the code: ",response.status_code)