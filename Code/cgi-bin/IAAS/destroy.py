#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os
import commands

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
	a=cookie["OS"].value
	c=[]
	b=[]
	a=str(a)
	h=commands.getoutput("sudo virsh destroy "+a)
	h=commands.getoutput("sudo virsh undefine "+a)
	h=commands.getoutput("sudo rm -rf /myos/"+a+ ".img")
	cursor.execute("select SL from "+uid+ " where OSNAME=%s",(a))
	mariadb_connection.commit()
	for SL in cursor:
		b=SL
	cursor.execute("delete from "+uid+ " where OSNAME=%s",(a))
	mariadb_connection.commit()
	cursor.execute("select SL from "+uid)
	mariadb_connection.commit()
	for SL in cursor:
		c=SL
		if(c[0]>b[0]):
			c=str(c[0])
			cursor.execute("update "+uid+ " set SL=SL-1 where SL=%s",(c))
			mariadb_connection.commit()
		
	mariadb_connection.close()
	print "location:http://192.168.0.8/cgi-bin/iaas.py"
	print ""
	
			
		
		
