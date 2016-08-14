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
			cursor.execute("select USERNAME from COOKIE where CNO=%s",(a))
			mariadb_connection.commit() 
			for USERNAME in cursor:
				b=USERNAME
				uid=b[0]
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
	cursor.execute("select OSNAME from "+uid+ " where SL=1");
	mariadb_connection.commit()
	for OSNAME in cursor:
		b=OSNAME
		name=b[0]
	cursor.execute("select MPORT from "+uid+ " where SL=1");
	mariadb_connection.commit()
	for MPORT in cursor:
		b=MPORT
		mprt=b[0]
	try:	
		name
		mprt
		mprt=str(mprt)
		cookie=Cookie.SimpleCookie()
		cookie["OS"]=name
		print cookie
	
		print "location:http://192.168.0.8/cgi-bin/dispos.py?q="+mprt
		print ""

	except:
		print "location:http://192.168.0.8/cgi-bin/iaas.py"
		print ""
	
