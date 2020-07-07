import requests
import json

response = requests.get("http://localhost:8000/v1/healthchecks/ping")

print("response status is {}".format(response.status_code))

print("response body is")

if response.status_code == 200:
    print(json.dumps(response.json(), indent=4))
else:
    print(response.text)
