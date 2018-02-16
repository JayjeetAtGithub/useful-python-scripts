import requests
from bs4 import BeautifulSoup


URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"
r=requests.get(URL)
soup = BeautifulSoup(r.content,"html5lib")
# print(soup.find_all(class_="mw-headline"))
# print(soup.find_all(id=True))
# print(soup.select(".tocnumber")[4].text)
#print(soup.find_all('ul')[14])

for lang in soup.find_all('ul')[14].select('li > a:nth-of-type(1)') :
	print("#",lang.text)

# for heading in soup.find_all('h2'):
# 	print(heading.text)
# print(len(soup.find_all(True)))
# print(soup.find("div")["class"])


# print(soup.title)
# print(soup.title.string)
# print(soup)
# print(type(soup))
# print(soup.prettify())



#soup = BeautifulSoup("<!DOCTYPE html><html><head><title>abcd</title></head><body>hi</body></html>","html5lib")
