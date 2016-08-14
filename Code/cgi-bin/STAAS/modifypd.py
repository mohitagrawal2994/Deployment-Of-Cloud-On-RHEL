#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os
import cgi
import commands

print "Content-type: text/html"
x=cgi.FieldStorage()
size=x.getvalue('size')
typ=x.getvalue('type')

size=cgi.escape(size)
typ=cgi.escape(typ)

mariadb_connection = mariadb.connect(user='root') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")
b=[]
flag=1
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
				name=b[0]
				cursor.execute("select FULLNAME from USERS where USERNAME=%s",(b[0]))
				mariadb_connection.commit()
				for FULLNAME in cursor:
					b=FULLNAME
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
	try:	
		cursor.execute("select USERNAME from PD where USERNAME=%s",(name))
		mariadb_connection.commit()
		for USERNAME in cursor:
			b=USERNAME
			pd=b[0]
			if(pd != name):
				flag=1
							
	except Exception as e:
		flag=1
	
	if(flag==1):
		mariadb_connection.close()
		print "location:http://192.168.0.8/cgi-bin/nstaas.py"
		print ""	
	else:
		
