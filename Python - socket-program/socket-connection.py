import socket
import sys
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket Successfully Created")

except socket.error as err:
	print("Socket Connection Failed")
   

ip = socket.gethostbyname('www.google.com')
print(ip)
port = 80
s.connect((ip,port))


