import socket
import sys
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket Created')
#host = socket.gethostname()
host = ''
port = 9999

s.bind((host,port)) #Passing an empty string means that the server can listen to incoming connections from other computers as well. 
print('socket binded to port ',port)
s.listen(5)
print('socket is listening')
while True:
	c, addr = s.accept()
	c.send(str.encode('thanks for your response server'))
	c.close()
