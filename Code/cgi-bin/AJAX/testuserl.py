#!/usr/bin/python

import cgi
import random
import MySQLdb as mariadb

print "Content-type:text/html"
x=cgi.FieldStorage()
name=x.getvalue('q')
print ""

flag=0;
if (name == ""):
	print " "
else:
	a=[]
	mariadb_connection = mariadb.connect(user='root') 
	cursor = mariadb_connection.cursor()
	cursor.execute("use lk") 
	cursor.execute("select USERNAME from USERS")
	mariadb_connection.commit()
	for USERNAME in cursor :
		a=USERNAME ;
		if(a[0] != name):
			flag=1
		else:
			flag=0
			break;
	if(flag == 1):
		print "Not A Valid User"
	
	
