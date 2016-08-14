#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os
import cgi

print "Content-type:text/html"
x=cgi.FieldStorage()
mprt=x.getvalue('q')

mariadb_connection = mariadb.connect(user='root') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")
b=[]
name=[]
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
	name=str(name)
	os.system("echo http://192.168.0.8/vnc/vnc.html?autoconnect=true\&port="+mprt+ " | qrencode -s 10x10 -o ../../html/Tar/"+name+ "/"+name+ ".png")
	print ""
	print """
	  <link rel=stylesheet type="text/css" href="../../css/base.css"  >
	  <link rel=stylesheet type="text/css" href="../../css/bar.css"  >
	  <style>
	  .misc
	  {
	    margin-left:1100px;
            width:15%;
          }
	  #qrcode
	  {
	    position:absolute;	
	    top:170px;
	    left:200px;
	  }
	  #qrmsg
	  {
	    position:absolute;	
	    top:330px;
	    left:900px;
	  }
	  </style>
	  <body style="background:url('http://192.168.0.8/backgrounds/Body7.jpg') no-repeat top left;">
	   <div class="head">
	     <div class="nhead">LEGACY<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;KLOUD</div>
           </div>
           <div class="misc">
             <a class="menu" href="../services.py">Services</a>
           </div>
	   <div id="qw" name="qw">
	     <span style="font-size:18px; margin-left:120px;">"""
print """<div id="wq" name="wq"><img src=http://192.168.0.8/pic/"""+uid  
print """ height="30" width="30"></img></div>Welcome"""
print uid
print"""</span>
	   </div>
	   <div id="list" name="list">
	     <ul id="chng" name="chng">
	       <li style="font-size:20px;"><img src="http://192.168.0.8/backgrounds/set.png"></img>Settings
		<ul style="margin-right:60px;margin-top:6px;">	       
	         <li><a href="../update.py" >Update Details</a></li>
	         <li><a href="../chpass.py" >Change Password</a></li>
		 <li><a href="../delete.py" onclick="return del();" >Delete My Account</a></li>
		 <li><a href="../logout.py" >Logout</a></li>
	       </ul></li>
             </ul>
	   </div>
	   <div id="qrcode" name="qrcode" >"""
print """<img src="http://192.168.0.8/Tar/"""
print name
print "/"
print name
print """.png"></img></div>
		<div id="qrmsg" name="qrmsg">
		  <b style="color:black;"><i>Scan The QR Code To Shift <br> The Operating System From <br> The Current Web Browser To Your Phone/Tablet</i></b>
		</div>	
	"""
