import requests
import notify2
import time
import os
from bs4 import BeautifulSoup
while True:
	url  = "https://weather.com/en-IN/weather/today/l/3b6be69a2d06426c709d7890d0300f99b5f792910485e325895ee6f2231c7545"
	r = requests.get(url)
	soup = BeautifulSoup(r.content,"html5lib")
	# print(soup.select(".today_nowcard-temp")[0].text)
	# print(soup.select(".today_nowcard-phrase")[0].text)
	# print(soup.select(".today_nowcard-feels")[0].text)
	ICON_PATH = os.getcwd() + "/icon1.ico"
	notify2.init("Weather Notifier")
	n = notify2.Notification("Today's Weather" , soup.select(".today_nowcard-temp")[0].text+"\n"+soup.select(".today_nowcard-phrase")[0].text+"\n"+soup.select(".today_nowcard-feels")[0].text,icon=ICON_PATH)
	n.set_urgency(notify2.URGENCY_NORMAL)
	n.set_timeout(2000)

	#n.update()
	n.show()
	time.sleep(120)


