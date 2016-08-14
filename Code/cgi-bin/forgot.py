#!/usr/bin/python

import MySQLdb as mariadb
import os
import cgi

print "Content-type:text/html"

x=cgi.FieldStorage()
uid=x.getvalue('uid')
ph=x.getvalue('ph')
pass1=x.getvalue('pass1')
pass2=x.getvalue('pass2')

uid=cgi.escape(uid)
ph=cgi.escape(ph)
pass1=cgi.escape(pass1)
pass2=cgi.escape(pass2)

if((uid=="")| (pass1=="")| (pass2=="")| (ph=="")):
	print "location:http://192.168.0.8/forgot.html"
	print ""

if((len(pass1)<6)| (len(pass2)<6)| (len(pass1)>30)| (len(pass2)>30)):
	print "location:http://192.168.0.8/forgot.html"
	print ""

if(pass1 != pass2):
	print "location:http://192.168.0.8/forgot.html"
	print ""

mariadb_connection = mariadb.connect(user='root') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")

b=[]
flag=1
uid=str(uid)
ph=str(ph)
	
try:
	cursor.execute("select PHONE from USERS where USERNAME=%s",(uid));
	mariadb_connection.commit()
	for PHONE in cursor:
		b=PHONE
		c=b[0]
		if(c==ph):
			flag=0
		else:
			flag=1
except(e):
	mariadb_connection.close()
	flag=1


if(flag==0):
	cursor.execute("update USERS set PASSWORD=%s where USERNAME=%s",(pass1,uid))
	mariadb_connection.commit()
	mariadb_connection.close()
	print "location:http://192.168.0.8/index.html"
	print ""
else:
	mariadb_connection.close()
	print "location:http://192.168.0.8/forgot.html"
	print ""
		
