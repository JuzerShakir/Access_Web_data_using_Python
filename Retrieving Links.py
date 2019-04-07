""" Exercise 4 """

# libraries for connecting to host, port, sending request
import urllib.request, urllib.error, urllib.parse
# for making html beautiful
from bs4 import BeautifulSoup

url = input('Enter url - ')

# connects to host and port and reads, returns string (UTF-8) format
html = urllib.request.urlopen(url).read()
# makes the html beautiful and easy to work with
soup = BeautifulSoup(html, 'html.parser')

# extracts all anchor tags for links, outputs a list
tags = soup('a')

# loops anchor tags in a list
for tag in tags:
    # extracts links and prints it
    print(tag.get('href', None))

# THE END