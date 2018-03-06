import sqlite3
import matplotlib.pyplot as plt
x = []
y = []
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

def create():
	c.execute('CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY , year INTEGER , items INTEGER) ')

def insert():
	c.execute('INSERT INTO table1(year,items) VALUES (?,?)' ,(2009,20))
	c.execute('INSERT INTO table1(year,items) VALUES (?,?)' ,(2010,45))

	c.execute('INSERT INTO table1(year,items) VALUES (?,?)' ,(2011,34))

	c.execute('INSERT INTO table1(year,items) VALUES (?,?)' ,(2014,12))

	c.execute('INSERT INTO table1(year,items) VALUES (?,?)' ,(2017,78))

	c.execute('INSERT INTO table1(year,items) VALUES (?,?)' ,(2018,49))
	conn.commit()


def read_from_db():
	c.execute('SELECT year,items FROM table1')
	data = c.fetchall()
	for row in data:
		x.append(row[0])

	for row in data:
		y.append(row[1])
	



read_from_db()
plt.plot(x,y)
plt.xlabel('Year')
plt.ylabel('No. of items sold')
plt.title('Sales Analytics')
plt.show()