""" Exercise 13 """

# URLlib for connecting to host and port of website, requesting data.
# JSON for data interchanging, lightweight version of XML
import urllib.parse, urllib.error, urllib.request, json

# google maps API to connect
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

# keeps asking for location until no input by user
while True:
    # asking for location
    address = input('Enter location : ')
    # breaks loop
    if len(address) < 1: break

    # converts the address string into link format type and appends with the google maps api URL
    # output a string of url
    url = serviceurl + urllib.parse.urlencode(
        {'address' : address})

    print('Retrieving...', url)

    # connects to site, reads it, and converts from UTF-8 to Unicode string, output is string
    data = urllib.request.urlopen(url).read().decode()
    print('Retrieved', len(data), 'characters!')

    # loads json format if no errors occur
    try:
        js = json.loads(data)
    except:
        js = None

    # if fails to load JSON, if 'status' in JSON is not OK dont continue... re ask for address
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure to Retrieve ====')
        print(data)
        continue

    # prints json form with some indentation
    print(json.dumps(js, indent=4))

    # extracting latitude and longitude of location entered from JSON
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']

    print('Latitude is :', lat, 'and Longitude is :', lng)

    location = js['results'][0]['formatted_address']
    print(location)