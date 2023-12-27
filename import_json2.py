import json

input_file1='coffee_sales/coffee_sales_1.json'
input_file2='coffee_sales/coffee_sales_2.json'

output_file='output.json'

with open(input_file1) as f:
    data1=json.load(f)

with open(input_file2) as f:
    data2=json.load(f)

cdata=[]
cdata.extend(data1)
cdata.extend(data2)

with open(output_file,'w') as f:
    json.dump(cdata,f)