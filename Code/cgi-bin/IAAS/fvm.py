#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import cgi
import random
import commands
import os

print "Content-type:text/html"

x=cgi.FieldStorage()
osname=x.getvalue('osname')
flav=x.getvalue('flav')

osname=cgi.escape(osname)
flav=cgi.escape(flav)

mariadb_connection = mariadb.connect(user='root') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")
b=[]
flag=0
count=1
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

		else:
			flag=1

except(Cookie.CookieError, KeyError):
	flag=1


if(flag==1):
	mariadb_connection.close()
	print "location:http://192.168.0.8/index.html"
	print ""

if((os=="")| (flav=="")):
	mariadb_connection.close()
	print "location:http://192.168.0.8/cgi-bin/iaas.py"
	print ""

else:
	cursor.execute("select SL from "+uid)
	mariadb_connection.commit()
	for SL in cursor:
		count+=1

	def func():
		z=random.randint(5900,9999)
		cursor.execute("select PORT from "+uid)
		mariadb_connection.commit()
		for PORT in cursor:
			b=PORT
			if(z==b[0]):
				func()
		return z
			
	def func1():
		y=random.randint(1000,9999)
		cursor.execute("select MPORT from "+uid)
		mariadb_connection.commit()
		for MPORT in cursor:
			b=MPORT
			if(y==b[0]):
				func1()
		return y

	z=func()
	y=func1()

	if(osname=="Redhat Enterprise Linux 5.7"):
		osn="rhel5.7"+uid
		pth="/var/www/html/OS/rhel5.7.iso"
	elif(osname=="Redhat Enterprise Linux 6.6"):
		osn="rhel6.4"+uid
		pth="/var/www/html/OS/rhel6.6.iso"
	elif(osname=="Redhat Enterprise Linux 7.0"):
		osn="rhel7"+uid
		pth="/var/www/html/OS/rhel7.iso"
	elif(osname=="Fedora Live"):
		osn="fedlive"+uid
		pth="/var/www/html/OS/fedlive.iso"
	elif(osname=="Fedora 18"):
		osn="fed18"+uid
		pth="/var/www/html/OS/fed18.iso"
	elif(osname=="Ubuntu 14.10"):
		osn="ubun14"+uid
		pth="/var/www/html/OS/ubuntu14.iso"
	elif(osname=="Windows XP Professional"):
		osn="winxp"+uid
		pth="/var/www/html/OS/winxp.iso"
	elif(osname=="Kali Linux 1.0.2"):
		osn="kali"+uid
		pth="/var/www/html/OS/kalilinux.iso"
	elif(osname=="CentOS 6.5"):
		osn="cen6.5"+uid
		pth="/var/www/html/OS/centos6.5.iso"
	else:
		osn="linmint"+uid
		pth="/var/www/html/OS/linmint10.iso"

	if(flav=="Small"):
		r="256"
		h="5"
	elif(flav=="Medium"):
		r="512"
		h="10"
	else:
		r="1024"
		h="15"

	cursor.execute("insert into "+uid+ "(SL,OSNAME,PORT,MPORT) values(%s,%s,%s,%s)",(count,osn,z,y))
	mariadb_connection.commit()
	mariadb_connection.close()

	z=str(z)
	y=str(y)
	
	hello = commands.getoutput("sudo virt-install --name="+osn+ " --ram="+r+ " --vcpus=1 --cdrom="+pth+ " --disk path=/myos/"+osn+ ".img,size="+h+ " --graphics=vnc,listen=0.0.0.0,port="+z+ " --noautoconsole");

	print "location:http://192.168.0.8/cgi-bin/iaas.py"
	print ""	

