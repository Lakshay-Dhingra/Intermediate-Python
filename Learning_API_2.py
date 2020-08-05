import requests
import json
parameters={"lat":-20,"lon":90}
response=requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(response.json())
