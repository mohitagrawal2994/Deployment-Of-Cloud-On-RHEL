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
	    left:45px;
	    color:green;
      	  }
	  #osl2
	  {
	    position:absolute;
	    top:260px;
	    left:50px;
	  }
	  #crt
	  {
	    position:absolute;
	    top:200px;
	    left:400px;
	  }
	  #mdfy
	  {
	    position:absolute;
	    top:380px;
	    left:400px;
	  }
	  #midline						/*Styling For The Midline*/
	  {
	    position:absolute;
	    top:170px;
	    left:900px;
	  }
	  #gostor
	  {
	    position:absolute;
	    top:370px;
	    left:1130px;
	  }
	  </style>
          <script>
	    function getstor()
	    {
	      var xmlhttp = new XMLHttpRequest();
	      xmlhttp.open("GET", "http://192.168.0.8/cgi-bin/STAAS/pdgetstor.py", false);
              xmlhttp.send();
	    }
	  </script>
	  </head>
	 <body style="background:url('http://192.168.0.8/backgrounds/Body4.jpg') no-repeat top left;">
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
	     <span style="font-size:30px; position:absolute; top:80px; left:230px; color:white;"><i><b>Storage As A Service</b></i></span>
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
	   <a id="osl1" name="osl1" href="http://192.168.0.8/cgi-bin/nstaas.py"><button type="button" style="font-size:30px; color:red; padding:20px; background-color:green; padding-left:40px; padding-right:40px;">PD</button></a>
	   <a id="osl2" name="osl2" href="http://192.168.0.8/cgi-bin/hstaas.py"><button type="button" style="font-size:30px; color:red; padding:20px; padding-left:40px; padding-right:40px;">HDD</button></a>
	   </div>
	   <div id="crt" name="crt">
	     <form method="post" action="http://192.168.0.8/cgi-bin/STAAS/createpd.py" autocomplete="off">
	       <fieldset style="border:double;color:gold;"><legend>CREATE STORAGE</legend>
	       <div style="padding:20px;">
	         SIZE(GB) : 
		 <select id="size" name="size">
		 <option>1</option>
		 <option>2</option>
		 <option>3</option>
		 <option>4</option>
		 <option>5</option>
		 <option>6</option>
		 <option>7</option>
		 <option>8</option>
		 <option>9</option>
		 <option>10</option>
		 <option>11</option>
		 <option>12</option>
		 <option>13</option>
		 <option>14</option>
		 <option>15</option>
		 <option>16</option>
		 <option>17</option>
		 <option>18</option>
		 <option>19</option>
		 <option>20</option>
		 <option>21</option>
		 <option>22</option>
		 <option>23</option>
		 <option>24</option>
		 <option>25</option>
		 <option>26</option>
		 <option>27</option>
		 <option>28</option>
		 <option>29</option>
		 <option>30</option>
		 <option>31</option>
		 <option>32</option>
		 <option>33</option>
		 <option>34</option>
		 <option>35</option>
		 <option>36</option>
		 <option>37</option>
		 <option>38</option>
		 <option>39</option>
		 <option>40</option>
		 <option>41</option>
		 <option>42</option>
		 <option>43</option>
		 <option>44</option>
		 <option>45</option>
		 <option>46</option>
		 <option>47</option>
		 <option>48</option>
		 <option>49</option>
		 <option>50</option>
		 <option>51</option>
		 <option>52</option>
		 <option>53</option>
		 <option>54</option>
		 <option>55</option>
		 <option>56</option>
		 <option>57</option>
		 <option>58</option>
		 <option>59</option>
		 <option>60</option>
		 <option>61</option>
		 <option>62</option>
		 <option>63</option>
		 <option>64</option>
		 <option>65</option>
		 <option>66</option>
		 <option>67</option>
		 <option>68</option>
		 <option>69</option>
		 <option>70</option>
		 <option>71</option>
		 <option>72</option>
		 <option>73</option>
		 <option>74</option>
		 <option>75</option>
		 <option>76</option>
		 <option>77</option>
		 <option>78</option>
		 <option>79</option>
		 <option>80</option>
		 <option>81</option>
		 <option>82</option>
		 <option>83</option>
		 <option>84</option>
		 <option>85</option>
		 <option>86</option>
		 <option>87</option>
		 <option>88</option>
		 <option>89</option>
		 <option>90</option>
		 <option>91</option>
		 <option>92</option>
		 <option>93</option>
		 <option>94</option>
		 <option>95</option>
		 <option>96</option>
		 <option>97</option>
		 <option>98</option>
		 <option>99</option>
		 </select>&nbsp;&nbsp;&nbsp;
		 <input type="submit" style="border-radius:40px; color:yellow; background-color:black;"></input>
	       </div>
	       </fieldset>
	     </form>
	   </div>
	   <div id="mdfy" name="mdfy">
	     <form method="post" action="http://192.168.0.8/cgi-bin/STAAS/modifypd.py" autocomplete="off">
	       <fieldset style="border:double;color:gold;"><legend>MODIFY STORAGE</legend>
	       <div style="padding:20px;">
	         Extend SIZE : <input type="radio" id="type" name="type" value="ext" required></input>
	         Reduce SIZE : <input type="radio" id="type" name="type" value="red" required></input><br><br>
	         Final SIZE(GB) : 
		 <select id="size" name="size">
		 <option>1</option>
		 <option>2</option>
		 <option>3</option>
		 <option>4</option>
		 <option>5</option>
		 <option>6</option>
		 <option>7</option>
		 <option>8</option>
		 <option>9</option>
		 <option>10</option>
		 <option>11</option>
		 <option>12</option>
		 <option>13</option>
		 <option>14</option>
		 <option>15</option>
		 <option>16</option>
		 <option>17</option>
		 <option>18</option>
		 <option>19</option>
		 <option>20</option>
		 <option>21</option>
		 <option>22</option>
		 <option>23</option>
		 <option>24</option>
		 <option>25</option>
		 <option>26</option>
		 <option>27</option>
		 <option>28</option>
		 <option>29</option>
		 <option>30</option>
		 <option>31</option>
		 <option>32</option>
		 <option>33</option>
		 <option>34</option>
		 <option>35</option>
		 <option>36</option>
		 <option>37</option>
		 <option>38</option>
		 <option>39</option>
		 <option>40</option>
		 <option>41</option>
		 <option>42</option>
		 <option>43</option>
		 <option>44</option>
		 <option>45</option>
		 <option>46</option>
		 <option>47</option>
		 <option>48</option>
		 <option>49</option>
		 <option>50</option>
		 <option>51</option>
		 <option>52</option>
		 <option>53</option>
		 <option>54</option>
		 <option>55</option>
		 <option>56</option>
		 <option>57</option>
		 <option>58</option>
		 <option>59</option>
		 <option>60</option>
		 <option>61</option>
		 <option>62</option>
		 <option>63</option>
		 <option>64</option>
		 <option>65</option>
		 <option>66</option>
		 <option>67</option>
		 <option>68</option>
		 <option>69</option>
		 <option>70</option>
		 <option>71</option>
		 <option>72</option>
		 <option>73</option>
		 <option>74</option>
		 <option>75</option>
		 <option>76</option>
		 <option>77</option>
		 <option>78</option>
		 <option>79</option>
		 <option>80</option>
		 <option>81</option>
		 <option>82</option>
		 <option>83</option>
		 <option>84</option>
		 <option>85</option>
		 <option>86</option>
		 <option>87</option>
		 <option>88</option>
		 <option>89</option>
		 <option>90</option>
		 <option>91</option>
		 <option>92</option>
		 <option>93</option>
		 <option>94</option>
		 <option>95</option>
		 <option>96</option>
		 <option>97</option>
		 <option>98</option>
		 <option>99</option>
		 </select><br><br>
	         <input type="submit" style="border-radius:40px; color:yellow; background-color:black;" ></input>
	       </div>
	       </fieldset>
	     </form>
	   </div>	
	   <div id="midline" name="midline">
	     <svg height="480" width="10">
	       <line x1="0" y1="0" x2="0" y2="480" style="stroke:rgb(255,255,255);stroke-width:10" />
	     </svg>
	   </div>
	   <a id="gostor" name="gostor" href='http://192.168.0.8/Tar/"""
print name
print "/"
print name
print """.tar.gz' onclick="getstor();" download><button type="button" style="font-size:20px; padding:20px; border-radius:15px; color:yellow; background-color:black;" >Get Storage</button></a>
"""
