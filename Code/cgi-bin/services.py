#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os

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

print """   <head>
	    <script src="../js/delete.js"></script>
	    <script>
	    var xAngle=0, yAngle=0;
	    function whichButton(event) 
	    {
	      switch(event.keyCode) 
              {
                case 37:
                yAngle -=90;
                break;
      
      		case 38:
      		xAngle +=90;
      		break;
   
      		case 39:
       		yAngle +=90;
      		break;

      		case 40:
                xAngle -=90;
     		break;
    	    };
            document.getElementById("cube").style.transform = "rotateX("+xAngle+"deg) rotateY("+yAngle+"deg)";
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
	  #container										/*Styling For The 3D Cube */
  	   {
    	     perspective: 1000px;
    	     perspective-origin: 50% 50%;
	     position:absolute;
	     top:300px ;
	     left:400px ;
 	   }
  	   #cube
  	   {
    	     position: relative;
    	     margin:0 auto;
    	     height: 100px;
    	     width: 100px;
    	     transition: transform 2s linear;
    	     transform-style: preserve-3d;
  	   }
  	   .face 
  	   {
   	     position: absolute;
             height: 200px;
             width: 200px;
             padding: 20px;
             background-color:rgba(0, 0, 0, 0.9);
             border:2px solid red;
  	   }
 	   #cube .one  
  	   {
             transform: rotateX(90deg) translateZ(130px);
  	   }
 	   #cube .two
 	   {
    	     transform: translateZ(130px);
  	   }
 	   #cube .three
  	   {
   	     transform: rotateY(90deg) translateZ(130px);
 	   }
 	   #cube .four
  	   {
  	     transform: rotateY(180deg) translateZ(130px);
  	   }
  	   #cube .five
  	   {
             transform: rotateY(-90deg) translateZ(130px);
 	   }
 	   #cube .six
 	   {
   	     transform: rotateX(-90deg) translateZ(130px) rotate(180deg);
 	   }
	   .xyz											/*Styling For The Hyperlinks On Cube*/
           {
             text-decoration:none;
	     font-size:30px ;
	     color:white;  
           }
	   .xyz:hover
	   {
	     color:gold;
	   }
	   #zxy											/*Styling For The Service On Cube*/
	   {
	     font-size:40px ;
	     margin-top:50px ;
	     color:white;
	   }
	 </style>
	 </head>
	 <body onkeyup="whichButton(event)" style="background:url('http://192.168.0.8/backgrounds/Body2.jpg') no-repeat top left;">
	   <div class="head">
	     <div class="nhead">LEGACY<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;KLOUD</div>
           </div>
           <div class="misc">
             <a class="menu" href="services.py">Services</a>
           </div>
	   <div id="qw" name="qw">
	     <span style="font-size:18px; margin-left:120px;">"""
print """<div id="wq" name="wq"><img src="http://192.168.0.8/pic/"""+uid  
print """" height="30" width="30"></img></div>Welcome"""
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
	   <div id="container">
  	     <div id="cube">
    	       <div class="face one">
     	       </div>
    	       <div class="face two">
      	         <center id="zxy" name="zxy"><b><i><u>SERVICES</u></i></b></center><br><br><center style="color:white;">Press &uarr;, &darr;, &larr; & &rarr; to Rotate <br>and <br>Click to Select</center>
               </div>
    	       <div class="face three">
      	         <a href="lsaas.py" class="xyz"><center><img src="http://192.168.0.8/backgrounds/saas.png" height="150" width="150"></img><br>SAAS</center></a>
               </div>
               <div class="face four">
		<a href="nstaas.py" class="xyz"><center><img src="http://192.168.0.8/backgrounds/staas.png" height="150" width="150"></img><br>STAAS</center></a> 
               </div>
    	       <div class="face five">
      	         <a href="iaas.py" class="xyz"><center><center><img src="http://192.168.0.8/backgrounds/iaas.png" height="150" width="150"></img><br>IAAS</center></a>
               </div>
               <div class="face six">
	       </div>
  	     </div>
	   </div>
         </body></html>""" 
