from zipfile import ZipFile
file_name = "Automate_the_Boring_Stuff_onlinematerials.zip"
with ZipFile(file_name,'r') as zip:
	zip.printdir()
	print("Extracting all files....")
	zip.extractall()
	print('Done!')
	# data = zip.read(name_of_file_to_read) #to read some specific file
	