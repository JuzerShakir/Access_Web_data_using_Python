""" Exercise 12 """

# lightweight version of XML
import json

# list of dictionaries
data = '''
[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    },
    {
        "id" : "009",
        "x" : "7",
        "name" : "Chuck"
    }
]'''

# passing data into json, output type is a list
info = json.loads(data)
print('Length of list is', len(info), end='\n\n')

# extracting values from each element
for item in info:
    print('Name:', item['name'])
    print('ID:', item['id'])
    print('x:', item['x'], end='\n\n')

# THE END