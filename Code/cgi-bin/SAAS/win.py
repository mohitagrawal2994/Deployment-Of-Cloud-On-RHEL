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
				cursor.execute("select FULLNAME from USERS where USERNAME=%s",(b[0]))
				mariadb_connection.commit()
				for FULLNAME in cursor:
					b=FULLNAME
					uid=b[0]
					flag=0
				cursor.execute("select PASSWORD from COOKIE where USERNAME=%s",(b[0]))
				mariadb_connection.commit()
				for PASSWORD in cursor:
					c=PASSWORD
					pass1=c[0]

		else:
			flag=1

except(Cookie.CookieError, KeyError, e):
	flag=1


if(flag==1):
	mariadb_connection.close()
	print "location:http://192.168.1.36/index.html"
	print ""

print ""
os.system("sudo mkdir ../../html/Tar/"+uid);
os.system("sudo cp run.bat ../../html/Tar/"+uid);
os.system("sudo cp READMEWIN ../../html/Tar/"+uid);
os.system("sudo cp putty.exe ../../html/Tar/"+uid);
os.system("sudo cp Xming.exe ../../html/Tar/"+uid);
os.system("sudo cp Xmingfonts.exe ../../html/Tar/"+uid);
os.system("sudo sed -i 's/root/"+uid+ "/g' ../../html/Tar/"+uid+ "/run.bat");
os.system("sudo sed -i 's/redhat/"+pass1+ "/g' ../../html/Tar/"+uid+ "/run.bat");
os.system("sudo tar -cvzf ../../html/Tar/"+uid+ "/"+uid+ ".tar.gz ../../html/Tar/"+uid+ "/run.bat ../../html/Tar/"+uid+ "/READMELIN ../../html/Tar/"+uid+ "/putty.exe ../../html/Tar/"+uid+ "/Xming.exe ../../html/Tar/"+uid+ "/Xmingfonts.exe");
