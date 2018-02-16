import requests
file_url = "https://static.googleusercontent.com/media/www.google.com/en//googleblogs/pdfs/google_predicting_the_present.pdf"
r= requests.get(file_url,stream = True)
with open("python_download.pdf","wb") as pdf:
	for chunk in r.iter_content(chunk_size = 1024):
		if chunk:
			pdf.write(chunk)


