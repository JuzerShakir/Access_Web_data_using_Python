""" Exercise 6 """

# libraries for connecting to host, port, sending request and regular expression
import urllib.request, urllib.error, urllib.parse, re
# for making html beautiful
from bs4 import BeautifulSoup

url = input("Enter URL - ")
# number of times visting links
reps = input("Enter reps - ")
# which link to visit from url
pos = input("Enter position - ")

# converting from str to int type
reps = int(reps)
pos = int(pos)

# list of names of visited sites
names = list()

# loop variable
i = 0

# will continue extract links from a site until otherwise
while i <= reps:
    # taken this step to able to have last url visited
    visit_link = url
    print(visit_link)

    # extracting name from link, gives a list
    name = re.findall("by_([A-z]+)", visit_link)
    # appends list to list, resulting in list of list
    names.append(name)

    # connects to host and port and reads, returns string (UTF-8) format
    html = urllib.request.urlopen(visit_link).read()
    # makes the html beautiful and easy to work with
    soup = BeautifulSoup(html, 'html.parser')

    # extracts all anchor tags for links, outputs a list
    tags = soup('a')

    # list to have all the links in a page visited
    links = list()

    # loops anchor tags in a list
    for tag in tags:
        # extracts links
        link = tag.get('href', None)
        # adds to list
        links.append(link)

    # extracting link from the list, decreamented value of pos since list counting starts from 0
    url = links[pos - 1]

    i = i + 1

# list of list
#print(names)

# extracts last name
last_name = names[-1][0]
print("Last name in sequence:", last_name)
