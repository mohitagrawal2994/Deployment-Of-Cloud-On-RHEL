#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os

print "Content-type:text/html"

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
			flag=0

		else:
			flag=1

except(Cookie.CookieError, KeyError):
	flag=1


if(flag==1):
	mariadb_connection.close()
	print "location:http://192.168.0.8/index.html"
	print ""
else:
	print ""
	try:
		cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
		a=cookie["OS"].value
		os.system("sudo virsh start "+a)

	except(Cookie.CookieError, KeyError):
		flag=1	
