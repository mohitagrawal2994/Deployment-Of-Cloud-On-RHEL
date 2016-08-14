#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os
import cgi

print "Content-type:text/html"

mariadb_connection = mariadb.connect(user='root') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")
b=[]
flag=0
try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	a=cookie["OS"].value
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
	count=0;
	c=[]
	cursor.execute("select SL from "+uid)
	mariadb_connection.commit()
	for SL in cursor:
		count+=1
	
	a=cookie["OS"].value
	a=str(a)
	cursor.execute("select SL from "+uid+ " where OSNAME=%s",(a))
	mariadb_connection.commit()
	for SL in cursor:
		b=SL
		sl=b[0]
	
	if(sl>1):
		sl-=1	
	else:
		sl=count
	
	cursor.execute("select OSNAME from "+uid+ " where SL=%s",(sl))
	mariadb_connection.commit()
	for OSNAME in cursor:
		c=OSNAME

	cookie=Cookie.SimpleCookie()
	cookie["OS"]=c[0]
	print cookie

	cursor.execute("select MPORT from "+uid+ " where SL=%s",(sl))
	mariadb_connection.commit()
	for MPORT in cursor:
		c=MPORT

	c=str(c[0])
	print "location:http://192.168.0.8/cgi-bin/dispos.py?q="+c
	print ""
		
			 
	
