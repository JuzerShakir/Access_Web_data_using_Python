""" Exercise 2 """

# libraries for connecting to host, port, sending request and regular expression
import urllib.request, urllib.parse, urllib.error, re
# for making html beautiful
from bs4 import BeautifulSoup

url = input('Enter URL - ')

# connects to host and port and reads
html = urllib.request.urlopen(url).read()
# makes the html beatiful and easy to work with
soup = BeautifulSoup(html, 'html.parser')

# extracts all span tags
tags = soup('span')

# for calculation
total = 0

# loops through all span tags
for tag in tags:
    # print(tag)
    # print(type(tag))

    # converting class type to string for regular expression to work
    s_tag = str(tag)
    # print(type(s_tag))

    # extracting digits, output type is list
    num = re.findall("[0-9.]+", s_tag)
    # print(type(num))

    # extracting element from the list and converting to int type
    num = int(num[0])
    # print(type(num))

    # calculation
    total = total + num

# final output
print(total)

# THE END