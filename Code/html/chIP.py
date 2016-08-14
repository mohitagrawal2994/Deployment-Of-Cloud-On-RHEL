#!/usr/bin/python

import os

os.system("sed -i 's/192.168.0.6/192.168.0.8/g' index.html")
os.system("sed -i 's/192.168.0.6/192.168.0.8/g' register.html")
os.system("sed -i 's/192.168.0.6/192.168.0.8/g' forgot.html")


