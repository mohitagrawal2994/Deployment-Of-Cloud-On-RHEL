#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os
import cgi
import commands

print "Content-type: text/html"
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
		os.system("sudo cp run.py ../../html/Tar/"+uid);
		os.system("sudo cp READMELIN ../../html/Tar/"+uid);
		os.system("sudo cp out.py ../../html/Tar/"+uid);
		os.system("sudo sed -i 's/redhat/"+uid+ "/g' ../../html/Tar/"+uid+ "/run.py");
		os.system("sudo sed -i 's/redhat/"+uid+ "/g' ../../html/Tar/"+uid+ "/out.py");
		os.system("sudo tar -cvzf ../../html/Tar/"+uid+ "/"+uid+ ".tar.gz ../../html/Tar/"+uid+ "/run.py ../../html/Tar/"+uid+ "/out.py ../../html/Tar/"+uid+ "/READMELIN");
