#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os
import cgi

print "Content-type:text/html"
x=cgi.FieldStorage()
mprt=x.getvalue('q')

mprt=cgi.escape(mprt)
mariadb_connection = mariadb.connect(user='root') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")
b=[]
name=[]
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
				cursor.execute("select FULLNAME from USERS where USERNAME=%s",(name))
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
	cursor.execute("select PORT from "+name+ " where MPORT=%s",(mprt))
	mariadb_connection.commit()
	for PORT in cursor:
		b=PORT
		prt=b[0]
	prt=str(prt)
	mprt=str(mprt)
	os.system("../html/websockify-master/./run "+mprt+ " 192.168.0.8:"+prt+ "&")
	print ""
	print """
	  <link rel=stylesheet type="text/css" href="../css/base.css"  >
	  <link rel=stylesheet type="text/css" href="../css/bar.css"  >
	  <style>
	  .misc
	  {
	    margin-left:1100px;
            width:15%;
          }
	  #vnc
	  {
	    position:absolute;
	    top:180px;
	    margin-left:0px;
	    
	  }
	  #controls
	  {
	    position:absolute;
	    height:355px;
	    width:200px;
	    top:325px;
	    left:1250px;
	  }
	  #strt
	  {
	    position:absolute;
	    top:50px;
	    left:25px;
	  }
	  #shtdwn
	  {
	    position:absolute;
	    top:50px;
	    left:125px;
	  }
	  #froff
	  {
	    position:absolute;
	    top:140px;
	    left:25px;
	  }
	  #dstry
	  {
	    position:absolute;
	    top:140px;
	    left:125px;
	  }
	  #prev
	  {
	    position:absolute;
	    top:240px;
	    left:35px;
	  }
	  #next
	  {
	    position:absolute;
	    top:240px;
	    left:125px;
	  }
	  #jump
	  {
	    position:absolute;
	    top:300px;
	    left:65px;
	  }
	  </style>
	  <script>
	    function start()
	    {
	      var xmlhttp = new XMLHttpRequest();
	      xmlhttp.open("GET", "http://192.168.0.8/cgi-bin/IAAS/start.py", false);
              xmlhttp.send();
	    }
	    function shutdown()
	    {
	      var xmlhttp = new XMLHttpRequest();
	      xmlhttp.open("GET", "http://192.168.0.8/cgi-bin/IAAS/shutdown.py", false);
              xmlhttp.send();
	    }
	    function forceoff()
	    {
	      var xmlhttp = new XMLHttpRequest();
	      xmlhttp.open("GET", "http://192.168.0.8/cgi-bin/IAAS/forceoff.py", false);
              xmlhttp.send();
	    }
	  </script>
	  <body style="background:url('http://192.168.0.8/backgrounds/Body6.jpeg') no-repeat top right;">
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
	   <div id="vnc" name"vnc">
	     <iframe src="http://192.168.0.8/vnc/vnc.html?autoconnect=true&port="""
print mprt
print """ "width="1100px" height="680px"></iframe></div>
	   </div>
	   <div id="controls" name"controls" style="box-shadow:15px 15px 50px blue; border-radius:10px;">
	     <p style="position:absolute;top:0px;left:30px;font-family:magneto; color:black;"><b><i>CONTROL BOX</i></b></p>
	     <div id="strt" name="strt">
	       <img src="http://192.168.0.8/backgrounds/poweron.png" onclick="start()" height="50" width="50" title="Power On"></img>
	     </div>
	     <div id="shtdwn" name="shtdwn">
	       <img src="http://192.168.0.8/backgrounds/shutdown.png" onclick="shutdown()" height="50" width="50" title="Shutdown"></img>
	     </div>
	     <div id="froff" name="froff">
	       <img src="http://192.168.0.8/backgrounds/forceoff.png" onclick="forceoff()" height="50" width="50" title="Force Off"></img>
	     </div>
	     <div id="dstry" name="dstry">
	       <a href="http://192.168.0.8/cgi-bin/IAAS/destroy.py"><img src="http://192.168.0.8/backgrounds/destroy.png" height="50" width="50" title="Delete OS"></img></a>
	     </div>
	     <div id="prev" name="prev">
	        <a href="http://192.168.0.8/cgi-bin/IAAS/previous.py"><button type="button" style="font-size:17px;" title="Previous OS"><</button></a>
	     </div>
	     <div id="next" name="next">
	        <a href="http://192.168.0.8/cgi-bin/IAAS/next.py"><button type="button" style="font-size:17px;" title="Next OS">></button></a>	
	     </div>
	     <div id="jump" name="jump">
	     	<a href="http://192.168.0.8/cgi-bin/IAAS/jump.py?q="""
print mprt
print """"><button type="button" style="font-size:17px;" title="Shift OS">JUMP</button></a>
	     </div>
	   </div>
	 </body>
       </html>
	"""

