""" Exercise 2 """

# importing necessory libraries for connecting to servers and port of a site
import urllib.request, urllib.error, urllib.parse

# connects to server and url and opens, fhand is a 'byte' class (UTF-8)
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

# reads through text of the file line by line
for line in fhand:
    # converts 'byte' class (UTF-8) to 'string' class (Unicode), deletes extra spaces before and after each line and prints
    print(line.decode().strip())

# THE END