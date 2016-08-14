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

print ""

print """
	  <link rel=stylesheet type="text/css" href="../css/base.css"  >
	  <link rel=stylesheet type="text/css" href="../css/bar.css"  >
	  <script src="../js/delete.js"></script>
	  <style>
	  .misc
	  {
	    margin-left:1100px;
            width:15%;
          }
	  #ellp
	  {
	    position:absolute;
	    left:350px;
	  }
	  #osl
	  {
	    position:absolute;
	    top:150px;
	    height:500px;
	    margin-left:0px;
	    width:20%;
	    box-shadow:15px 15px 150px white;
          }
	  #osl1
	  {
	    position:absolute;
	    top:40px;
	    left:40px;
	    color:green;
      	  }
	  #osl2
	  {
	    position:absolute;
	    top:260px;
	    left:35px;
	  }
	  #fire
	  {
	    position:absolute;
	    top:300px;
	    left:500px ;
	  }
	  #note
	  {
	    position:absolute;
	    top:300px;
	    left:900px ;
	  }
	  #ff
	  {
	    position:absolute;
	    width:7%;
	    height:3%;
	    top:440px;
	    left:520px;
	  }
	  #np
	  {
	    position:absolute;
	    width:7%;
	    height:3%;
	    top:440px;
	    left:930px;
	  }
	  </style>
	  <script>
	    function fsaas()
	    {
	      var xmlhttp = new XMLHttpRequest();
	      xmlhttp.open("GET", "http://192.168.0.8/cgi-bin/SAAS/firefox.py", false);
              xmlhttp.send();
            }
	    function nsaas()
	    {
	      var xmlhttp = new XMLHttpRequest();
	      xmlhttp.open("GET", "http://192.168.0.8/cgi-bin/SAAS/notepad.py", false);
              xmlhttp.send();
            }
	  </script>
	  </head>
	 <body style="background:url('http://192.168.0.8/backgrounds/Body3.jpg') no-repeat top left;">
	   <div class="head">
	     <div class="nhead">LEGACY<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;KLOUD</div>
           </div>
           <div class="misc">
             <a class="menu" href="services.py">Services</a>
           </div>
	   <div id="qw" name="qw">
	     <span style="font-size:18px; margin-left:120px;">"""
print """<div id="wq" name="wq"><img src=http://192.168.0.8/pic/"""+uid  
print """ height="30" width="30"></img></div>Welcome"""
print uid
print"""</span>
	   </div>
	   <div id="ellp" name="ellp">
	     <svg height=400 width=700>
	     <ellipse cx=350 cy=100 rx=270 ry=40 style="opacity:0.9; fill:black; stroke:grey; stroke-width:5;" />
	     <span style="font-size:30px; position:absolute; top:80px; left:220px; color:white;"><i><b>Software As A Service</b></i></span>
             </svg>
	   </div>
	   <div id="list" name="list">
	     <ul id="chng" name="chng">
	       <li style="font-size:20px;"><img src="http://192.168.0.8/backgrounds/set.png"></img>Settings
		<ul style="margin-right:60px;margin-top:6px;">	       
	         <li><a href="update.py" >Update Details</a></li>
	         <li><a href="chpass.py" >Change Password</a></li>
		 <li><a href="delete.py" onclick="return del();" >Delete My Account</a></li>
		 <li><a href="logout.py" >Logout</a></li>
	       </ul></li>
             </ul>
	   </div> 
	   <div id="osl" name="osl">
	     <a id="osl1" name="osl1" href="http://192.168.0.8/cgi-bin/lsaas.py"><button type="button" style="font-size:30px; color:red; padding:20px; padding-left:50px; padding-right:50px; background-color:green;">LINUX</button></a>
	     <a id="osl2" name="osl2" href="http://192.168.0.8/cgi-bin/wsaas.py"><button type="button" style="font-size:30px; color:red; padding:20px;">WINDOWS</button></a>
	   </div>
	   <div id="fire" name="fire">
	   <img src="http://192.168.0.8/backgrounds/firefox.png" height="130px" width="130px"></img>
	   </div>
	   <div id="note" name="note">
	   <img src="http://192.168.0.8/backgrounds/notepad.png" height="130px" width="130px"></img>
	   </div>
	   <a id="ff" name="ff" href='http://192.168.0.8/Tar/"""
print name
print "/"
print name
print""".tar.gz' onClick="fsaas();" download><button type="button">Get Firefox</button></a>
	
	  <a id="np" name="np" href='http://192.168.0.8/Tar/"""
print name
print "/"
print name
print """.tar.gz' onClick="nsaas();" download><button type="button">Get Notepad</button></a>
	   </body>"""
