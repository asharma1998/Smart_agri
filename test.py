#!/usr/bin/python36

import cgi
print("content-type: text/html")
print("\n")

import subprocess as sp

form = cgi.FieldStorage()
cname = form.getvalue('cn')
#image = form.getvalue('img')

#cname = input("enter name")
container_name = sp.getstatusoutput("sudo ansible-playbook /root/shellinabox.yml --extra-vars='x={0}'".format(cname))


