import requests,json,base64,time

url = "http://10.10.9.2:3001/message"  # Change this URL to Jared's actual endpoint

message_request = {
  "body": {
    "message": "Jared is an amazing app"
  },
  "recipient": {
    "handle": "alex@prograde.space",
  }
}

payload = json.dumps(message_request)

headers = {
    "Content-Type": "application/json"
}

response = requests.request("POST",url,data = payload,headers = headers)
print(response.status_code)
print(response.text)
