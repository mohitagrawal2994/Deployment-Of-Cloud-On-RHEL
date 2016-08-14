#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os
import cgi
import commands

print "Content-type: text/html"
x=cgi.FieldStorage()
size=x.getvalue("size")

size=cgi.escape(size)

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
			if(pd==name):
				flag=1
				break
			
	except Exception as e:
		flag=1

	if(flag==1):
		mariadb_connection.close()
		print "location:http://192.168.0.8/cgi-bin/nstaas.py"
		print ""	
	else:
		hell=commands.getoutput("sudo lvcreate --name pd"+name+ " --size "+size+ "G myvg")
		hell=commands.getoutput("sudo mkfs.vfat /dev/myvg/pd"+name)
		hell=commands.getoutput("sudo mkdir /media/mystorage/"+name)
		hell=commands.getoutput("sudo chmod 777 /media/mystorage/"+name)
		hell=commands.getoutput("sudo echo /media/mystorage/"+name+ " *\(rw,no_root_squash,sync\) >> /etc/exports")
		hell=commands.getoutput("exportfs -r")
		hell=commands.getoutput("sudo mount /dev/myvg/pd"+name+ " /media/mystorage/"+name)
		cursor.execute("insert into PD(USERNAME,SIZE) values(%s,%s)",(name,size))
		mariadb_connection.commit()	
		mariadb_connection.close()
		print "location:http://192.168.0.8/cgi-bin/nstaas.py"
		print ""
	

