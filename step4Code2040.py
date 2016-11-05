import requests
import json

token = "c3922bf6cf1313e37768687dd70c3b21"
tokens = {"token": token}
header = {'Content-Type': 'application/json'}
prefixHTTP = 'http://challenge.code2040.org/api/prefix'

challenge_endpoint = "http://challenge.code2040.org/api/prefix/validate"
response1 = requests.post(prefixHTTP, data=json.dumps(tokens),headers=header).json()

#def task_two():
    
#print "Response from API: " + response1.text
prefix = response1["prefix"]
my_array = response1["array"]
result_array = []

for item in my_array:
	if not item.startswith(prefix):
		result_array.append(str(item))

prefixResult = {"token": token,"array":result_array}
response1 = requests.post(challenge_endpoint, data=json.dumps(prefixResult),headers=header)
print( response1.text)
