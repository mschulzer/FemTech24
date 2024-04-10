import requests
import json

url = "https://ml.dataekspeditioner.dk/add/"

payload = json.dumps({
  "email": "peaches@marioland.com",
  "state": "#fffccc"
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response) # e.g. <Response [200]>
