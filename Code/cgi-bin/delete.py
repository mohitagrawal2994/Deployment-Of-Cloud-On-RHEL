#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os
import cgitb

print "Content-type:text/html"
cgitb.enable()
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
		 	break
		else:
			flag=1

except (Cookie.CookieError, KeyError):
	flag=1

if(flag==1):
	mariadb_connection.close()
	print "location:http://192.168.0.8/index.html"
	print ""


cursor.execute("select USERNAME from COOKIE where CNO=%s",(a))
mariadb_connection.commit()
for USERNAME in cursor:
	b=USERNAME
	uid=b[0]
cursor.execute("delete from COOKIE where CNO=%s",(a))
mariadb_connection.commit()
cursor.execute("delete from USERS where USERNAME=%s",(b[0]))
mariadb_connection.commit()
cursor.execute("drop table "+uid)
mariadb_connection.commit()
os.system("sudo userdel "+uid)

print "location:http://192.168.0.8/index.html"
print ""



