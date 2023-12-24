import requests
import json

url='https://edfreitas.me/test/wired_brain.json'

headers={
    'Content-Type':'application/json'
}

params={
    'location':'London',
    'start_date':'2021-03-01',
    'end_date':'2021-03-31'
}

response=requests.get(url,headers=headers,params=params)
if response.status_code==200:
    data= json.loads(response.text)
    for item in data:
        print(item)
else:
    print("error fetching data with the code: ",response.status_code)