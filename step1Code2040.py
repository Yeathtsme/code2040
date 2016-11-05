import requests
import json 

token = "c3922bf6cf1313e37768687dd70c3b21"
repository = "https://github.com/Yeathtsme/code2040"
header = {'Content-Type': 'application/json'}
'''
Connects to the CODE2040 challenge endpoint and sends the required
data in JSON format. 
For step 1 of the CODE2040 API Challenge
'''
#tokens = {"token": token}
def connect():
    # Connect to the challenge endpoint
    challenge_endpoint = "http://challenge.code2040.org/api/register"

    # Send JSON with token and github repository
    jsons = {"token" : token, 
            "github" : repository}
    response = requests.post(challenge_endpoint, data=json.dumps(jsons),headers=header)
    print "Response from API: " + response.text


connect()
