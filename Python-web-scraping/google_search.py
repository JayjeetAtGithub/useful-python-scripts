try:
	from googlesearch import search
except ImportError :
	print("No Module Found")

query = "GeeksForGeeks"
for j in search(query,tld="co.in",num=10,stop=1,pause=2):
	print(j)
	#break -- add the break statement to get the first link 
