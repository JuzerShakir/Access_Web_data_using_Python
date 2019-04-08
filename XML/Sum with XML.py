""" Exercise 10 """

# XML library
import xml.etree.ElementTree as ET
# libraries for connecting to host, port, sending request
import urllib.parse, urllib.error, urllib.request


url = input('Enter URL - ')

# connects to host and port and reads, returns string (UTF-8) format
data = urllib.request.urlopen(url).read()

# read data, returns as tree structured object
tree = ET.fromstring(data)

# # finds every 'count' tags inside 'comments/comment' parent tag, returns list of tags
counts = tree.findall('comments/comment/count')

# print(len(counts))

# for computation
total = 0

for count in counts:
    # extracts text from 'count' tag, converts numbers to int type, adds to total 
    total = total + int(count.text)

# final output    
print(total)

# THE END