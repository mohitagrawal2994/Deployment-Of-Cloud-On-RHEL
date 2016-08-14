#!/usr/bin/python

import MySQLdb as mariadb
import Cookie
import random
import cgi
import cgitb
import datetime
import os

print "Content-type:text/html"
cgitb.enable()
x=cgi.FieldStorage()
uid=x.getvalue('uid')
passx=x.getvalue('passx')

uid = cgi.escape(uid)
passx = cgi.escape(passx)

if ((uid=="") | (passx=="")):
	print "location:http://192.168.0.8/index.html"
	print ""

if ((len(uid)>30) | (len(passx)<6) | (len(passx)>30)):
	print "location:http://192.168.0.8/index.html"
	print ""

mariadb_connection = mariadb.connect(user='root') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk") 
cursor.execute("select USERNAME from USERS")
mariadb_connection.commit()
a=[]
b=[]
flag=0
for USERNAME in cursor :
	a=USERNAME ;
	if(uid==a[0]):
		cursor.execute("select PASSWORD from USERS where USERNAME=%s",(uid))
		mariadb_connection.commit()
		for PASSWORD in cursor :
			b=PASSWORD ;
		if(b[0]==passx):
			flag=1;
			break
	
if(flag==0):
	print "location:http://192.168.0.8/index.html"
	print ""
else:
	z=random.randint(0,1000000000)
	future=datetime.datetime.now()+datetime.timedelta(days=1)
	cursor.execute("insert into COOKIE(CNO,USERNAME,PASSWORD,AUTOLOGOUT) values(%s,%s,%s,%s)",(z,uid,passx,future))
	mariadb_connection.commit()
	cookie=Cookie.SimpleCookie()
	cookie["LegacyKloud"]=z
	print cookie
	os.system("sudo mkdir -p ../html/Tar/"+uid);
	os.system("sudo chmod 777 ../html/Tar/"+uid);
	print "location:http://192.168.0.8/cgi-bin/services.py"
	print ""
			

