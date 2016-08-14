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
			  cursor.execute("select FULLNAME from USERS where USERNAME=%s",(b[0]))
			  mariadb_connection.commit()
			  for FULLNAME in cursor:
			  	b=FULLNAME
				uid=b[0]
				flag=0
				break
		else:
			flag=1
except (Cookie.CookieError, KeyError):
	flag=1

mariadb_connection.close()
if(flag==1):
	print "location:http://192.168.0.8/index.html"
	print ""

print ""
print """  <script src="../js/delete.js"></script>
	   <script src="../js/cpass.js"></script>
	   <script>
	   function pmt()							//Function To Check Valid Details Filled In The Form
           {
             var a = document.getElementById('pass1').value;
             var b = document.getElementById('pass2').value;
             var c = 0 ;
             if((a.length>=6)&&(b.length>=6))
             {
               if( a != b )
               {
	         alert('Entered Passwords Do Not Match');       	
	         c = 1;
               }
             }
             else
             {
	       alert("The Password Should Be A Minimum Of 6 characters")
	       c = 1;
             }
	     if(c==1)
      	     {
       	       return false ;
     	     }
           }
	   </script>
	   <link rel=stylesheet type="text/css" href="../css/base.css"  >
	   <link rel=stylesheet type="text/css" href="../css/bar.css"  >
	   <style>
	   .misc
	   {
	     margin-left:1100px;
	     width:15%;
           }
           #posq
	   {
	     position:absolute ;
	     top:240px ;
	     left:300px ;
	   }
	   #pos
	   {
	     border-radius:30px;
	     position:relative ;
	     font-size:25px ;
	     color:lightblue;
	     font-family:magneto;
	     box-shadow: 15px 0px 140px lightskyblue;
	     padding:20px ;
	     width:350px ;
	   }
	 </style>
         <body style="background:url('http://192.168.0.8/backgrounds/Body2.jpg') no-repeat top left;">
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
	   <div id="posq" name="posq">
	     <form id="pos" name="pos" method="post" onsubmit="return pmt();" action="http://192.168.0.8/cgi-bin/chpass1.py">
	       Old Password:<br>
	       <input type="Password" id="opass" name="opass" size="30" maxlength="30" placeholder="Enter Old Password" autofocus></input><br><br>
	       New Password:<br>
	       <input type="Password" id="pass1" name="pass1" size="30" maxlength="30" placeholder="Enter New Password"></input><br><br>
	       Re-Type New Password:<br>
	       <input type="Password" id="pass2" name="pass2" size="30" maxlength="30" placeholder="Re-Type New Password"></input><br><br>
	       <input type="submit" value="Submit" onclick="return cpass();"></input>
	     </form>
           </div>
	 </body>
	</html>"""
