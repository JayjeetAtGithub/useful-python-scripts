from googlesearch import search
from tkinter import *
import requests


def download():
	urllist = []
	s_query = entry.get()
	query = "filetype:pdf" + " " + s_query + " " + "ebook"
	for j in search(query,tld="co.in",num=10,stop=1,pause=2):
		
			urllist.append(j)

	 

	print(urllist)
	file_url=urllist[0]
	r=requests.get(file_url,stream = True)
	with open('mybook.pdf','wb') as pdf:
		for chunk in r.iter_content(chunk_size = 1024):
			if chunk:
				pdf.write(chunk)


	print("Book Downloaded Succesfully")

root = Tk()
v = StringVar()
root.geometry("600x200+0+0")
root.title("Automatic Book Downloader")
label = Label(root,text="Enter Book Name:",padx = 2,pady = 2).grid(row=1,column=0)
entry = Entry(root,bd=2,textvariable=v,width=40)
entry.grid(row=1,column=1)

button = Button(root,bd=2,command=download,text="Download").grid(row=1,column=2)
	
root.mainloop()




