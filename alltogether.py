import json
import requests
import os
import argparse  #define command line arguments 

parser=argparse.ArgumentParser(description='command line app to fetch,retrieve,read,import and parse json data')
# print(parser)

parser.add_argument('--fetch',metavar='URL',help='fetch json data from a url')
parser.add_argument('--api',metavar='ENDPOINT',help='retrieve json data froma a web api')
parser.add_argument('--read',metavar='PATH',help='read json data from a file')
parser.add_argument('--importjson',metavar='PATH',help='import json data from a file and convert to a python data structure')
parser.add_argument('--parse',metavar='PATH',help='describe and parse json data from a file')
args=parser.parse_args()

if args.fetch:
    url=args.fetch
    response=requests.get(url)
    data=response.json()
    print(json.dumps(data,indent=4))

if args.api:
    endpoint=args.api
    response=requests.get(endpoint)
    data=response.json()
    print(json.dumps(data,indent=4))

if args.read:
    path=args.read
    with open(path) as f:
        data=json.load(f)
        print(json.dumps(data,indent=4))

if args.importjson:
    path=args.importjson
    with open(path) as f:
        data=json.load(f)
        if isinstance(data,list):
            print('list')
            print(data)

        elif isinstance(data,dict):
            print('dict')
            print(data)
        else:
            print('data')
            print(data)

if args.parse:
    path=args.parse
    with open(path) as f:
        data=json.load(f)
        print('Type: ',type(data))
        if isinstance(data,list):
            print('list')
            for item in data:
                print(item)
        elif isinstance(data,dict):
            print('dict')
            for key,value in data.items():
                 print(key,':',value)
        else:
            print('data')
            print(data)


#type these in the terminal
#py alltogether.py --fetch https://edfreitas.me/test/wired_brain.json
'''
[
    {
        "id": 1,
        "date": "2021-03-01",
        "location": "London",
        "sales": 327
    },
    {
        "id": 4,
        "date": "2021-03-02",
        "location": "London",
        "sales": 275
    },
    {
        "id": 7,
        "date": "2021-03-03",
        "location": "London",
        "sales": 312
    },
    {
        "id": 10,
        "date": "2021-03-04",
        "location": "London",
        "sales": 289
    },
    {
        "id": 13,
        "date": "2021-03-05",
        "location": "London",
        "sales": 337
    }
]
'''
#py alltogether.py --read coffee_sales/coffee_sales.json
'''
{
    "locations": [
        {
            "id": 1,
            "name": "New York"
        },
        {
            "id": 2,
            "name": "London"
        },
        {
            "id": 3,
            "name": "Tokyo"
        }
    ],
    "sales": [
        {
            "id": 1,
            "location_id": 1,
            "date": "2021-01-01",
            "sales": 100
        },
        {
            "id": 2,
            "location_id": 1,
            "date": "2021-01-02",
            "sales": 200
        },
        {
            "id": 3,
            "location_id": 2,
            "date": "2021-01-01",
            "sales": 150
        },
        {
            "id": 4,
            "location_id": 2,
            "date": "2021-01-02",
            "sales": 250
        },
        {
            "id": 5,
            "location_id": 3,
            "date": "2021-01-01",
            "sales": 120
        },
        {
            "id": 6,
            "location_id": 3,
            "date": "2021-01-02",
            "sales": 180
        }
    ]
}
'''
#py alltogether.py --parse coffee_sales/coffee_sales.json
'''
Type:  <class 'dict'>
dict
locations : [{'id': 1, 'name': 'New York'}, {'id': 2, 'name': 'London'}, {'id': 3, 'name': 'Tokyo'}]        
sales : [{'id': 1, 'location_id': 1, 'date': '2021-01-01', 'sales': 100}, {'id': 2, 'location_id': 1, 'date': '2021-01-02', 'sales': 200}, {'id': 3, 'location_id': 2, 'date': '2021-01-01', 'sales': 150}, {'id': 4, 'location_id': 2, 'date': '2021-01-02', 'sales': 250}, {'id': 5, 'location_id': 3, 'date': '2021-01-01', 'sales': 120}, {'id': 6, 'location_id': 3, 'date': '2021-01-02', 'sales': 180}]
'''


