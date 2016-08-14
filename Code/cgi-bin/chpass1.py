#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os
import cgi
import cgitb
 
print "Content-type: text/html"
cgitb.enable()

x=cgi.FieldStorage()
opass=x.getvalue('opass')
pass1=x.getvalue('pass1')
pass2=x.getvalue('pass2')

opass = cgi.escape(opass)
pass1 = cgi.escape(pass1)
pass2 = cgi.escape(pass2)

if(pass1 != pass2):
	print "location:http://192.168.0.8/cgi-bin/chpass.py"
	print ""

if((len(opass)<6)| (len(opass)>30)| (len(pass1)<6)| (len(pass1)>30)| (len(pass2)<6)| (len(pass2)>30)):
	print "location:http://192.168.0.8/cgi-bin/chpass.py"
	print ""

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

cursor.execute("select PASSWORD from COOKIE where CNO=%s",(a))
mariadb_connection.commit()
for PASSWORD in cursor:
	b=PASSWORD
if(b[0]==opass):	
	flag=0
	cursor.execute("select USERNAME from COOKIE where CNO=%s",(a))
	mariadb_connection.commit()
	for USERNAME in cursor:
		b=USERNAME
else:
	flag=1

if(flag==1):
	mariadb_connection.close()
	print "location:http://192.168.0.8/cgi-bin/chpass.py"
	print ""   

cursor.execute("update COOKIE set PASSWORD=%s where USERNAME=%s",(pass1,b[0]))
mariadb_connection.commit()
cursor.execute("update USERS set PASSWORD=%s where USERNAME=%s",(pass1,b[0]))
mariadb_connection.commit()
print "location:http://192.168.0.8/cgi-bin/services.py"
print ""


