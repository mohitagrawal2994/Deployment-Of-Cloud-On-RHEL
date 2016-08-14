#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os

print "Content-type: text/html"


mariadb_connection = mariadb.connect(user='root') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")
b=[]
c=[]
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
			cursor.execute("delete from COOKIE where CNO=%s",(a))
			mariadb_connection.commit();
			break
		else:
			flag=1
except (Cookie.CookieError, KeyError):
	flag=1

mariadb_connection.close()
os.system("sudo rm -rf ../html/Tar/"+uid);
print "location:http://192.168.0.8/index.html"
print ""

