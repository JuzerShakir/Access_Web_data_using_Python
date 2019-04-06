""" Exercise 1 """


# library necessory to make connections to servers
import socket

# makes doors and opens it
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# helps making bridge from door (pc) to server (host) and to its port
mysock.connect(('data.pr4e.org', 80))
# a get request for the webpage, encodes it from Unicode to UTF-8
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


while True:
    # will receive 512 character
    data = mysock.recv(512)
    # if no data, quit
    if len(data) < 1:
        break
    # outputs data by decoding from UTF-8 format to Unicode
    print(data.decode())

# connection close
mysock.close()