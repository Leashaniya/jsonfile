import requests
import json

url='https://edfreitas.me/test/wired_brain.json'
response=requests.get(url)
# result=response.json()
# for i in result:
#     print(i)

if response.status_code==200:
    data= json.loads(response.text)
    for item in data:
        print(item)
else:
    print("error fetching data with the code: ",response.status_code)