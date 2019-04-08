""" Exercise 9 """

# XML library
import xml.etree.ElementTree as ET

# string sample data
data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

# read sample data, returns as tree structured object
tree = ET.fromstring(data)
# finds every 'user' tags inside 'users' parent tag, returns list of tags
lst = tree.findall('users/user')

# elemnts in list
print(len(lst), end='\n\n')

# prints each user's name, id and attribute
for item in lst:
    print('Name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attribute', item.get('x'), end='\n\n')

# THE END