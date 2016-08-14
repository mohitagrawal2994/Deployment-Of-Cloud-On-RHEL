#!/usr/bin/python

import MySQLdb as mariadb
import cgi
import cgitb
import os
import commands

print "Content-type:text/html"
cgitb.enable()
x=cgi.FieldStorage()
fname=x.getvalue('fn')
uid=x.getvalue('uid')
pass1=x.getvalue('pass1')
pass2=x.getvalue('pass2')
dd=x.getvalue('dd')
mm=x.getvalue('mm')
yy=x.getvalue('yy')
gen=x.getvalue('gen')
eid=x.getvalue('eid')
ph=x.getvalue('ph')
fileitem=x['pp']

fname = cgi.escape(fname)
uid = cgi.escape(uid)
pass1 = cgi.escape(pass1)
pass2 = cgi.escape(pass2)
dd = cgi.escape(dd)
mm = cgi.escape(mm)
yy = cgi.escape(yy)
gen = cgi.escape(gen)
eid = cgi.escape(eid)
ph = cgi.escape(ph)

if(pass1 != pass2):
	print "location:http://192.168.0.8/register.html"
	print ""
if((fname=="")| (uid=="")| (pass1=="")| (pass2=="")| (dd=="")| (mm=="")| (yy=="")| (gen=="")| (eid=="")| (ph=="")):
	print "location:http://192.168.0.8/register.html"
	print ""
if((len(fname)>30)| (len(uid)>30)| (len(pass1)<6)| (len(pass1)>30)| (len(pass2)<6)| (len(pass2)>30) | (len(ph)>11)):
	print "location:http://192.168.0.8/register.html"
	print ""

if fileitem.filename:
	f = os.path.basename(uid)
        open('../html/pic/' + f, 'wb').write(fileitem.file.read())
else:
   os.system("sudo cp ../html/backgrounds/default.png ../html/pic/"+uid)

a=[]
flag=0

mariadb_connection = mariadb.connect(user='root') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk") 
cursor.execute("select USERNAME from USERS")
mariadb_connection.commit()
for USERNAME in cursor :
	a=USERNAME ;
	if(a[0] == uid):
		flag=1;
		break;
if(flag==1):
	mariadb_connection.close()		
	print "location:http://192.168.0.8/register.html"
	print ""
else:
	p=str(dd)
	q=str(mm)
	r=str(yy)
	cursor.execute("insert into USERS(USERNAME,PASSWORD,FULLNAME,DOB,GENDER,EMAILID,PHONE) values(%s,%s,%s,%s,%s,%s,%s)",(uid,pass1,fname,p+ "-"+q+ "-"+r,gen,eid,ph))
	mariadb_connection.commit()
	cursor.execute("create table "+uid+ " (SL INTEGER PRIMARY KEY NOT NULL, OSNAME varchar(37) NOT NULL, PORT INTEGER NOT NULL, MPORT INTEGER NOT NULL)");
	mariadb_connection.commit()
	mariadb_connection.close()
	os.system("sudo useradd "+uid)
	commands.getoutput("sudo echo "+pass1+ "| sudo passwd "+uid+ " --stdin") 
	print "location:http://192.168.0.8/index.html"
	print ""
	

