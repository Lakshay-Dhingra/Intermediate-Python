import requests
import json
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("http://api.open-notify.org/astros.json")
print(response)
if (response.status_code)==200:
    print(response.json())
    print(type(response.json()))
    jprint(response.json())
else:
    print("Some Problem ocurred...")
