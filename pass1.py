#!/usr/bin/python36

import cgi
print("content-type: text/html")
print("\n")

import subprocess as sp

form = cgi.FieldStorage()
language = form.getvalue('lang')

if language == "Python3":
      print("<a href='http://192.168.43.185:1234' target='f1'>Click here</a>")
      print("<iframe name='f1' height='300' width='800'></iframe>")
elif language == "Python2":
      print("<a href='http://192.168.43.185:2345' target='f1'>Click here</a>")
      print("<iframe name='f1' height='300' width='800'></iframe>")
else:
      print("<a href='http://192.168.43.185/java.html' target='f1'>Click here</a>")
      print("<iframe name='f1' height='300' width='800'></iframe>")



