import requests
url = "https://icanhazdad.joke.com/"
response = requests.get(url,headers={"Accept":"application/json"})
data = response.json()
print(data["joke"])
print(data["status"])