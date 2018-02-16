import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
r = requests.get(image_url)
with open("python_logo.png","wb") as file:
	file.write(r.content)

	#the image would be found at the place the script is located