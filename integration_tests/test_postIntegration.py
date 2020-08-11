import requests
import json


postresponse = requests.post('http://localhost:8000/v1/postexperiences', headers={'Content-Type': 'application/json'},
                data=json.dumps({'title': 'THIS IS FILE 1'}))

postresponse2 = requests.post('http://localhost:8000/v1/postexperiences', headers={'Content-Type': 'application/json'},
                data=json.dumps({'title': 'THIS IS THE FILE 2'}))



getresponse = requests.get("http://localhost:8000/v1/getexperiences/software")

def Print(response, type):
    print("info for the {} call".format(type))
    print("response status is {}".format(response.status_code))
    print("response body is")

    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
    else:
        print(response.text)


Print(postresponse, "POST")

Print(getresponse, "GET")


