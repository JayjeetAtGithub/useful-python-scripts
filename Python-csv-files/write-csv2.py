from csv import writer
with open("data.csv","w") as file:
	csv_writer = writer(file)
	csv_writer.writerow(["Name","Age"])
	csv_writer.writerow(["Jayjeet",18])
	csv_writer.writerow(["Ankan",19])
