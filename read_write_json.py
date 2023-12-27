import os
import json

dir='coffee_sales/'
cdata=[]

#gonna combine different json files in the coffee sales folder

for file in os.listdir(dir):
    # print(file)  #print the file names in coffee_sales folder
    if file.endswith('.json'):
        with open (os.path.join(dir,file),'r') as f:         #folder name and the current file name in the join  method
            data=json.load(f)
            cdata.extend(data)

for item in cdata:
    print(item)

outfile='outputs.json'

with open(outfile,'w') as f:
    json.dump(cdata,f)
    
