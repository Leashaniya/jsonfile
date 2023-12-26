import os
dir='coffee_sales/'

#list the name of the directories inside the specific folder

for file in os.listdir(dir):
    print(file)

print('\n')

# the files which name ends with .json 
for file in os.listdir(dir):
    if file.endswith('json'):
        print(file)