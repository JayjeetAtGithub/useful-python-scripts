import requests
#r = requests.get("https://api.github.com/")
r = requests.get("http://samples.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&appid=b6907d289e10d714a6e88b30761fae22")
data = r.json()
#print(data['hub_url'])
#print(data['keys_url'])
print(data['list'][5]['name'])
print(data['list'][4]['main']['pressure'])
#this way we can parse complex JSON Apis


