#!/usr/bin/python

import cgi
import random

print "Content-type:text/html"
x=cgi.FieldStorage()
pass1=x.getvalue('q')
print ""

if (len(pass1)<6):
	print "Min. 6 characters"
elif(len(pass1)>30):
	print "Within 30 characters" 
else:
	print ""
