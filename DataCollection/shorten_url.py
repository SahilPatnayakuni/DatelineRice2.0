import requests

response = requests.get("https://api-ssl.bitly.com/v3/shorten?access_token=TOKEN&login=USERNAME&longUrl=ENTERURLHERE")
jsonFile = response.json()

print(jsonFile['data']['url'])
