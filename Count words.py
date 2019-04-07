""" Exercise 3 """

# importing necessory libraries for connecting to servers and port of a site
import urllib.request, urllib.error, urllib.parse

# connects to server and url and opens, fhand is a 'byte' class (UTF-8)
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = dict()

# reads through text of the file line by line
for line in fhand:
    # converts 'byte' class (UTF-8) to 'string' class (Unicode), returns a list of words, each element as a list of words
    words = line.decode().split()
    # loops through list of word to count repeated words in a file
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# outputs answer
print(counts)