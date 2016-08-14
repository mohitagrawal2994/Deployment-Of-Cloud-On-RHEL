#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os

print "Content-type: text/html"


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
				break;

		else:
			flag=1

except(Cookie.CookieError, KeyError):
	flag=1


if(flag==1):
	mariadb_connection.close()
	print "location:http://192.168.1.36/index.html"
	print ""

print ""

os.system("sudo cp run.py ../../html/Tar/"+uid);
os.system("sudo cp READMELIN ../../html/Tar/"+uid);
os.system("sudo sed -i 's/root/"+uid+ "/g' ../../html/Tar/"+uid+ "/run.py");
os.system("sudo sed -i 's/firefox/notepad/g' ../../html/Tar/"+uid+ "/run.py");
os.system("sudo tar -cvzf ../../html/Tar/"+uid+ "/"+uid+ ".tar.gz ../../html/Tar/"+uid+ "/run.py ../../html/Tar/"+uid+ "/READMELIN");
print "1"
