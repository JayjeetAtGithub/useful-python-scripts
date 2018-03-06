import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT,keyword TEXT,value REAL)')


# def data_entry():
# 	c.execute('INSERT INTO stuffToPlot VALUES(145,"2016-01-01","pytohn",5)')
# 	c.close()
# 	conn.close()

def dynamic_data_entry(n1):
	unix = time.time()
	date = n1
	keyword = 'python'
	value = random.randrange(0,10)
	c.execute('INSERT INTO stuffToPlot(unix,datestamp,keyword,value) VALUES (?,?,?,?)' ,(unix,date,keyword,value))
	conn.commit()

def read_from_db():
	c.execute('SELECT keyword,unix,value,datestamp FROM stuffToPlot')
	data = c.fetchall()
	#print(data)
	for row in data:
		print(row[0] ,"|" , row[1] , "|" , row[2] , "|" , row[3])


def update_db():
	c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 3')
	conn.commit()



def delete_from_db():
	c.execute('DELETE FROM stuffToPlot WHERE value = 99 LIMIT 100')
	conn.commit()









# create_table()
# data_entry()

# for i in range(10):
# 	dynamic_data_entry("14-12-2014")
# 	time.sleep(1)
read_from_db()  
#it returns tuples within lists
c.close()
conn.close()
