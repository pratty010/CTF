#!/usr/bin/env python3

"""
Solution for the PicoCTF 2K19 Cryptography Challenge - Mr-Worldwide.

Description: A musician left us a message - message.txt. What's it mean?

Solution: The message is actually a set of coordinates. We can reverse them using an GeoPy API relying on google maps.

Flag: picoCTF{KODIAK_ALASKA}
"""


from geopy.geocoders import Nominatim

# Create a new Nominatim geolocator
geolocator = Nominatim(user_agent="shinchan")


input = [
"35.028309, 135.753082",
"46.469391, 30.740883",
"39.758949, -84.191605",
"41.015137, 28.979530",
"24.466667, 54.366669",
"3.140853, 101.693207",
"9.005401, 38.763611",
"-3.989038, -79.203560",
"52.377956, 4.897070",
"41.085651, -73.858467",
"57.790001, -152.407227",
"31.205753, 29.924526"
]

out = ""

for loc in input:
	# Use the reverse() method to get location details from coordinates
	location = geolocator.reverse(loc, language="en")

	print(location.raw['address'])
	if 'province' in location.raw['address']:
		out += (location.raw['address']['province'])[0]
	elif 'village' in location.raw['address']:
		out += (location.raw['address']['village'])[0]
	elif 'town' in location.raw['address']:
		out += (location.raw['address']['town'])[0]
	elif 'city' in location.raw['address']:
		out += (location.raw['address']['city'])[0]
	elif 'state' in location.raw['address']:
		out += (location.raw['address']['state'])[0]

print("picoCTF{" + out[:6] + "_" + out[6:] + "}")
