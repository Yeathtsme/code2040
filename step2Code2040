import requests
import json

token = "c3922bf6cf1313e37768687dd70c3b21"
tokens = {"token": token}
repository = "https://github.com/Yeathtsme/code2040"
header = {'Content-Type': 'application/json'}
reverseHTTP = 'http://challenge.code2040.org/api/reverse'
#d = requests.get('http://challenge.code2040.org/api/reverse').text
#string = d[::-1]
challenge_endpoint = "http://challenge.code2040.org/api/reverse/validate"
response1 = requests.post(reverseHTTP, data=json.dumps(tokens),headers=header)

#def task_two():
    
print "Response from API: " + response1.text
string = response1.text[::-1]
print(string)
reverseResult = {"token": token,"string":string}
response2 = requests.post(challenge_endpoint, data=json.dumps(reverseResult),headers=header)
print "Response from API: " + response2.text
