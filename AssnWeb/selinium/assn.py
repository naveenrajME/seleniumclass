import requests
import json
url = "https://api.thedogapi.com/v1/breeds"
 
response = requests.get(url)
data =response.text
parsed = json.loads(data)
with open('assn1.txt', 'w') as a:
    a.write(json.dumps(parsed, indent=4))
