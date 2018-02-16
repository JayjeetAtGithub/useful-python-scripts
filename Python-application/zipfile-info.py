from zipfile import ZipFile
import datetime
file_name = "Automate_the_Boring_Stuff_onlinematerials.zip"
with ZipFile(file_name,'r') as zip:
	for info in zip.infolist():
		print(info.filename)
		print(str(info.create_version))
		print(str(info.file_size))
		print(str(info.compress_size))
		print(str(info.create_system))
		if(str(info.create_system)=='0'):
			print("Windows")
		else:
			print("linux")

		print(str(datetime.datetime(*info.date_time)))