#Writing a dictionary

import csv
mydict = [{'branch':'cse','name':'jayjeet','year':'4'},
          {'branch':'ece','name':'souvik','year':'3'},
          {'branch':'ee','name':'deap','year':'2'},
          {'branch':'ce','name':'binayak','year':'4'},
          {'branch':'me','name':'saikat','year':'5'},
          {'branch':'bt','name':'sagarjyoti','year':'7'}]


fields = ['name','branch','year','cgpa']
filename = 'datadict.csv'
with open(filename,'w') as csvfile:
	writer = csv.DictWriter(csvfile,fieldnames = fields)
	writer.writeheader()
	writer.writerows(mydict)