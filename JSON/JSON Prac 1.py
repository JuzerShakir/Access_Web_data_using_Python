""" Exercise 11 """

# lightweight version of XML
import json

# dictionaries within a dictionary
data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

# passing data into json, output type is a dictionary
info = json.loads(data)

# extracts and outputs name
print('Name:', info['name'])
# extracts and outputs value of 'hide' key in email key
print('Hide:', info['email']['hide'])

# THE END