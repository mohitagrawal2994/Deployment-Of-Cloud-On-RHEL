#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os
import cgi

print "Content-type: text/html"
x=cgi.FieldStorage()
msg=cgi.getvalue('q')

mariadb_connection = mariadb.connect(user='root') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")
b=[]
flag=0
try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	a=cookie["LegacyKloud"].value
	cursor.execute("select CNO from COOKIE")
	mariadb_connection.commit()
	for CNO in cursor:
		b=CNO
		if(b[0] == a):
			cursor.execute("select USERNAME from COOKIE where CNO=%s",(a))
			mariadb_connection.commit() 
			for USERNAME in cursor:
				b=USERNAME
				uid=b[0]
				cursor.execute("select FULLNAME from USERS where USERNAME=%s",(b[0]))
				mariadb_connection.commit()
				for FULLNAME in cursor:
					b=FULLNAME
					flag=0

		else:
			flag=1

except(Cookie.CookieError, KeyError, e):
	flag=1


if(flag==1):
	mariadb_connection.close()
	print "location:http://192.168.1.36/index.html"
	print ""

print ""

if(msg == ""):
	print ""
else:
	if(msg == "Small"):
		print "CPU=1 RAM=256MB HDD=5GB"
	elif(msg == "Medium"):
		print "CPU=1 RAM=512MB HDD=10GB"
	else:
		print "CPU=1 RAM=1024MB HDD=15GB"
		
	
