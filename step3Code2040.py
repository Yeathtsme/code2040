#tier3.py
import requests
import json

#My Token
token = "c3922bf6cf1313e37768687dd70c3b21"

#	My Token in a Dictionary
tokens = {"token": token}

#	Github Account
repository = "https://github.com/Yeathtsme/code2040"

#	Header
header = {'Content-Type': 'application/json'}

#	Haystack Link
haystackLink = 'http://challenge.code2040.org/api/haystack'

#	Send Here
challenge_endpoint = "http://challenge.code2040.org/api/haystack/validate"

#	Calling API's json
response1 = requests.post(haystackLink, data=json.dumps(tokens),headers=header).json()    
#print "Response from API: " + response1
needle = response1['needle']
haystack = response1['haystack']
#print(needle)
#print(haystack)

#	Find the index of needles within haystack
index = haystack.index(needle)
#print(index)

haystackResult = {"token": token,"needle":index}

#	Post Answer Online
response1 = requests.post(challenge_endpoint, data=json.dumps(haystackResult),headers=header)   

#	Did I Complete Step?
print(response1.text)
