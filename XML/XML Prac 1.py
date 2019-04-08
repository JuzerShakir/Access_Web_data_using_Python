""" Exercise 8 """

# XML library
import xml.etree.ElementTree as ET

# string sample data
data = '''
<person>
    <name>Chuck</name>
    <phone type="int1">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

# read sample data, returns as tree structured object
tree = ET.fromstring(data)

# finds 'name' tag in a tree object, prints text within tags
print('Name:', tree.find('name').text)
# finds 'email' tag in a tree object, prints value of attr 'hide'
print('Attr:', tree.find('email').get('hide'))

# THE END