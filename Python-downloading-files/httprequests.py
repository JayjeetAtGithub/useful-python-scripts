import requests
r = requests.get("https://www.facebook.com")
print(r.content)
print(r.status_code)
print(r.text) 