import requests
import json
from datetime import datetime, timedelta

token = "c3922bf6cf1313e37768687dd70c3b21"
tokens = {"token": token}
header = {'Content-Type': 'application/json'}
datingHTTP = 'http://challenge.code2040.org/api/dating'

challenge_endpoint = "http://challenge.code2040.org/api/dating/validate"
response1 = requests.post(datingHTTP, data=json.dumps(tokens),headers=header).json()

datestamp = response1["datestamp"]
interval = response1["interval"]

receiveTime = datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")
newTime = receiveTime + timedelta(seconds=interval)
newFormatTime = newTime.strftime('%Y-%m-%dT%H:%M:%SZ')
    
#print "Response from API: " + response1.text


datingResult = {"token": token,"datestamp":newFormatTime}
response1 = requests.post(challenge_endpoint, data=json.dumps(datingResult),headers=header)
print( response1.text)
