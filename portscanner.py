#!/usr/bin/python

import socket
import sys
import os
import time
try:
	from datetime import datetime
except:
	print "Can't import datetime, maybe it doesn't installed yet"
	
os.system('clear')
class warna :
	HIJAU = '\033[92m'
	KUNING = '\033[92m'
	MERAH = '\033[31m'
	TUTUP = '\033[00m'
print warna.KUNING+
         ".*---------------------------------------*."
print "| [ Simple Port Scanner  ]  |"
print "|        INSIDE HEARTZ        |"
print "+-----------------------------------------+\n"+warna.TUTUP      
remoteServer = raw_input("Enter Your IP > ")
st = int(raw_input("Enter first value to scan > "))
en = int(raw_input("Enter last value to scan > "))
ok = en+1
remoteServerIP = socket.gethostbyname(remoteServer)
print "="*60
print "Scanning remote host",remoteServerIP
print "="*60

time1 = datetime.now()
times = time.asctime(time.localtime(time.time()))
try:
	for port in range(st,ok):
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		hasil = sock.connect_ex((remoteServerIP,port))
		#print "[",times,"] Now Scanning on port",port
		if (hasil == 0):
			print "[",times,"]"+warna.HIJAU+" Port {}: Open".format(port)+warna.TUTUP
		else:
			print "[",times,"]"+warna.MERAH+" Port {}: Closed".format(port)+warna.TUTUP
			sock.close()
except KeyboardInterrupt:
	print "You pressed ctrl+c"
	sys.exit()
except:
	print "Couldn't connect to",remoteServer
	sys.exit()
time2 = datetime.now()
total = time2-time1
print "Scanning completed in :",total