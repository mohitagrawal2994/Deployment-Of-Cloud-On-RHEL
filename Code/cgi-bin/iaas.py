#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os

print "Content-type:text/html"

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
	  #cvm
	  {
	    position:absolute;
	    top:160px;
	    left:300px;
	    font-size:20px;
	    font-family:cooper black;
	    color:gold;
	  }
	  #f1
	  {
	    position:absolute;
	    top:190px;
	    left:100px;
	  }
	  .f11
	  {
	    margin-left:50px;
	    margin-right:50px;
	  }
	  .f12
	  {
	    margin-left:50px;
	    margin-right:50px;
	  }
	  #midline						/*Styling For The Midline*/
	  {
	    position:absolute;
	    top:170px;
	    left:710px;
	  }
	  #govm							/* Position Of Launch VMs Button */
	  {
	    position:absolute;	
	    top:350px;
	    left:1000px;
	  }
	  </style>
	  </head>
	 <body style="background:url('http://192.168.0.8/backgrounds/Body5.jpg') no-repeat top left;">
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
	     <span style="font-size:30px; position:absolute; top:80px; left:190px; color:white;"><i><b>Infrastructure As A Service</b></i></span>
             </svg>
	   </div>
	   <div id="list" name="list">
	     <ul id="chng" name="chng">
	       <li style="font-size:20px;"><img src="http://192.168.0.8/backgrounds/set.png"></img>Settings
		<ul style="margin-right:50px;margin-top:6px;">	       
	         <li><a href="update.py" >Update Details</a></li>
	         <li><a href="chpass.py" >Change Password</a></li>
		 <li><a href="delete.py" onclick="return del();" >Delete My Account</a></li>
		 <li><a href="logout.py" >Logout</a></li>
	       </ul></li>
             </ul>
	   </div> 
	   <div id="cvm" name="cvm">
	     <b><i>Create VM</i></b>
	   </div>
	   <div id="f1" name="f1">
	     <form id="flf" name="flf" method="post" action="http://192.168.0.8/cgi-bin/IAAS/fvm.py" autocomplete="off">
	       <fieldset style="border:double;color:gold;"><legend>TYPICAL</legend>
	       <div class="f11"><pre style="font-size:15px;">Select OS       :  <select id="osname" name="osname">
	           <option>CentOS 6.5</option>
		   <option>Fedora 18</option>
		   <option>Fedora Live</option>
		   <option>Kali Linux 1.0.2</option>
		   <option>Linux Mint 10</option>
		   <option>Redhat Enterprise Linux 5.7</option>
	           <option>Redhat Enterprise Linux 6.6</option>
	           <option>Redhat Enterprise Linux 7.0</option>
	           <option>Ubuntu 14.10</option>
	           <option>Windows XP Professional</option>
		 </select><br><br>Select Flavour  :  <select id="flav" name="flav">
	           <option>Small</option>
		   <option>Medium</option>
	           <option>Large</option>
	         </select><br><br><input type="submit" style="border-radius:40px; color:yellow; background-color:black; "></input></pre></div>
	       </fieldset> 
	     </form><br>
	     <form id="nmf" name="nmf" method="post" action="http://192.168.0.8/cgi-bin/IAAS/nvm.py" autocomplete="off">
	       <fieldset style="border:double;color:gold;"><legend>CUSTOM</legend>	
	       <div class="f12"><pre style="font-size:15px;">Select OS :  <select id="osnam" name="osnam">
	           <option>CentOS 6.5</option>
		   <option>Fedora 18</option>
		   <option>Fedora Live</option>
		   <option>Kali Linux 1.0.2</option>
		   <option>Linux Mint 10</option>
		   <option>Redhat Enterprise Linux 5.7</option>
	           <option>Redhat Enterprise Linux 6.6</option>
	           <option>Redhat Enterprise Linux 7.0</option>
	           <option>Ubuntu 14.10</option>
	           <option>Windows XP Professional</option>
	         </select><br><br>CPU       :  <input id="cpu" name="cpu" type="text"></input><br><br>RAM       :  <input id="ram" name="ram" type="text"></input><br><br>HDD       :  <input id="hdd" name="hdd" type="text"></input><br><br><input type="submit" style="border-radius:40px; color:yellow; background-color:black; "></input></pre></div>
	       </fieldset>  
	     </form>
	   </div>
	   <div id="midline" name="midline">
	     <svg height="480" width="10">
	       <line x1="0" y1="0" x2="0" y2="480" style="stroke:rgb(255,255,255);stroke-width:10" />
	     </svg>
	   </div>
	   <a href="http://192.168.0.8/cgi-bin/IAAS/aport.py" id="govm" name="govm"><button type="button" style="font-size:20px; padding:20px; border-radius:15px; color:yellow; background-color:black;">Launch VMs</button></a>
	  """
